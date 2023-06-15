from fastapi import APIRouter
from sqlalchemy import select
from models.model_types import EdgeT
from models.edge import Edge
from models.node import Node
from models.graph import Graph
from config import db

edge_router = APIRouter(prefix='/edge')


@edge_router.post("/create")
async def post_edge(msg: EdgeT):
    # Verificar se o node1 (nó de origem) existe no banco de dados
    node1 = db.session.query(Node).filter(Node.id == msg.node1_id).first()
    if node1 is None:
        return {"error": "O nó de origem (node1) não existe no banco de dados."}

    # Verificar se o node2 (nó de destino) existe no banco de dados
    node2 = db.session.query(Node).filter(Node.id == msg.node2_id).first()
    if node2 is None:
        return {"error": "O nó de destino (node2) não existe no banco de dados."}

    # Verificar se o graph_id existe no banco de dados
    graph = db.session.query(Graph).filter(Graph.id == msg.graph_id).first()
    if graph is None:
        return {"error": "O ID do grafo (graph_id) não existe no banco de dados."}

    # Todas as verificações passaram, criar a nova aresta
    edge = Edge(
        weight=msg.weight,
        node1_id=msg.node1_id,
        node2_id=msg.node2_id,
        graph_id=msg.graph_id
    )

    db.session.add(edge)
    db.session.commit()
    db.session.close()

    return {
        "success": True,
        "weight": msg.weight,
        "from": msg.node1_id,
        "target": msg.node2_id,
        "graph_id": msg.graph_id
    }


@edge_router.get("/get/{id}")
async def get_node(id: int):
    edge = db.session.query(Edge).filter(Edge.id == id).first()
    return {edge}


@edge_router.delete("/delete")
async def delete_edge(id: dict):
    edges = db.session.execute(select(Edge).where(Edge.id == id["id"]))
    edge = [edge for edge in edges][0][0]
    db.session.delete(edge)
    db.session.commit()

    return {'success': 'Edge deleted successfully'}


@edge_router.put("/update")
async def update_edge(json: dict):
    edge = [edge for edge in db.session.execute(
        select(Edge).where(Edge.id == json["id"]))][0][0]
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
