from fastapi import APIRouter
from sqlalchemy import select
from models.model_types import EdgeT 
from models.node import Node, Edge
from models.graph import Graph
from config import db


edge_router = APIRouter(prefix='/edge')

@edge_router.post("/create")
async def post_edge(msg: EdgeT):
    msg =     {
            "id": 1,
            "x": 5,
            "y": 5,
            "first_node": True,
            "graph_id": 1,
            }
    msg.nodes = [
        Node( x = 3, y = 3, first_node = True, graph_id = msg.graph_id),
        Node( x = 5, y = 4, first_node = False, graph_id = msg.graph_id),
        Node( x = 2, y = 5, first_node = False, graph_id = msg.graph_id),
        Node( x = 5, y = 7, first_node = False, graph_id = msg.graph_id)
    ]
    # Verificar se o node1 (nó de origem) existe no banco de dados
    #node1 = db.session.query(Node).filter(Node.id == msg.node1_id).first()
    #if node1 is None:
      #  return {"error": "O nó de origem (node1) não existe no banco de dados."}
    
    # Verificar se o node2 (nó de destino) existe no banco de dados
    #node2 = db.session.query(Node).filter(Node.id == msg.node2_id).first()
   # if node2 is None:
       # return {"error": "O nó de destino (node2) não existe no banco de dados."}
    
    # Verificar se o graph_id existe no banco de dados
   # graph = db.session.query(Graph).filter(Graph.id == msg.graph_id).first()
    #if graph is None:
       # return {"error": "O ID do grafo (graph_id) não existe no banco de dados."}
    
    # Todas as verificações passaram, criar a nova aresta
    edge = Edge(
        weight=msg.weight,
        nodes=[msg.nodes],
        graph_id=msg.graph_id
    )

    db.session.add(edge)
    db.session.commit()
    db.session.close()
    
    return {
        "success": True,
        "weight": msg.weight,
        "nodes": msg.nodes,
        "graph_id": msg.graph_id
    }

@edge_router.get("/get/{name}")
async def get_edge(msg: EdgeT):
    pass

@edge_router.delete("/delete")
async def delete_edge(id:dict):
    edges = db.session.execute(select(Edge).where(Edge.id==id["id"]))
    edge = [edge for edge in edges][0][0]
    db.session.delete(edge)
    db.session.commit()

@edge_router.put("/update")
async def update_edge(json:dict):
    edge = [edge for edge in db.session.execute(select(Edge).where(Edge.id == json["id"]))][0][0]
    for key in json.keys():
        if key == "edge_id":
            edge.id = json["id"]
        elif key == "weight":
            edge.weight = json["weight"]
        elif key == "from":
            edge.node1_id = json["from"]
        elif key == "target":
            edge.node2_id = json["target"]

    db.session.commit()

    return {f"id:{edge.id}, weight:{edge.weight}, from:{edge.node1_id}, target:{edge.node2_id}, graph_id:{edge.graph_id}"}