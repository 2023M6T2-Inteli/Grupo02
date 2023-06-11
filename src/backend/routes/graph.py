from fastapi import APIRouter
from sqlalchemy import select
from models.model_types import GraphT 
from models.graph import Graph
from models.node import Node
from models.edge import Edge
from config import db

graph_router = APIRouter(prefix='/graph')
# uvicorn main:app --host 0.0.0.0 --port 8000
# @graph_router.get("/get/{id}")
# async def get_graph(id:int):
#     stm = select(Graph).where(Graph.id == id)
#     nodes = db.session.query(Node).filter(Node.id == id).all()
#     edges = db.session.query(Edge).filter(Edge.id == id).all()
#     graph = [graph for graph in db.session.execute(stm)][0][0]
#     return graph.return_json()

@graph_router.get("/get/{id}")
async def get_graph(id: int):
    stm = select(Graph).where(Graph.id == id)
    get_nodes = db.session.query(Node).filter(Node.graph_id == id).all()
    nodes = [nodes.return_json() for nodes in get_nodes]
    get_edges = db.session.query(Edge).filter(Edge.graph_id == id).all()
    edges = [edges.return_json() for edges in get_edges]
    
    for edge in edges:
        edge["from"] = {"x":nodes[edge["from"]]["x"],"y":nodes[edge["from"]]["y"]}
        edge["target"] = {"x":nodes[edge["target"]]["x"],"y":nodes[edge["target"]]["y"]}
    graph = [graph for graph in db.session.execute(stm)][0][0]

    graph_data = {
        "graph": graph.return_json(),
        "edges": [edge for edge in edges]
    }

    return graph_data

@graph_router.get('/get_all/')
async def get_all_graphs():
    graphs = db.session.query(Graph).all()
    graph_data = [graph.return_json() for graph in graphs]
    return graph_data

@graph_router.post("/create")
async def post_root(msg: GraphT):
    graphs = db.session.query(Graph).all()
    graph_data = [(graph.return_json()) for graph in graphs]
    for content in graph_data:
        if content["name"] == msg.name:
            return "Nome já cadastrado"



    graph = Graph(name = msg.name,
                  description = msg.description,
                  image_address = msg.image_address)

    db.session.add(graph)

    db.session.commit()
    db.session.close()
    
    return  {f"Sucessful create graph {msg.name}"}

@graph_router.delete("/delete")
async def delete_graph(name:dict):
   
    graphs = db.session.execute(select(Graph).where(Graph.name == name["name"]))
    graph = [graph for graph in graphs][0][0]
    db.session.delete(graph)
    db.session.commit()

@graph_router.put("/update")
async def update_graph(json:dict):
    graph = [graph for graph in db.session.execute(select(Graph).where(Graph.id == json["id"]))][0][0]
    for key in json.keys():
        if key == "name":
            graph.name = json["name"]
        elif key == "description":
            graph.description = json["description"]
        elif key == "image_address":
            graph.image_address = json["image_address"]
    db.session.commit()


    return {"eu sou otario"}

