from fastapi import APIRouter
from sqlalchemy import select
from models.model_types import GraphT 
from models.graph import Graph
from models.node import Node
from models.edge import Edge
from config import db

graph_router = APIRouter(prefix='/graph')

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
    nodes = db.session.query(Node).filter(Node.graph_id == id).all()
    edges = db.session.query(Edge).filter(Edge.graph_id == id).all()
    graph = [graph for graph in db.session.execute(stm)][0][0]

    graph_data = {
        "graph": graph.return_json(),
        "nodes": [node.return_json() for node in nodes],
        "edges": [edge.return_json() for edge in edges]
    }

    return graph_data


@graph_router.post("/create")
async def post_root(msg: GraphT):

    graph = Graph(name = msg.name,
                  description = msg.description,
                  image_address = msg.image_address)

    db.session.add(graph)

    db.session.commit()
    db.session.close()
    
    return  {f"nome:{msg.name}, descrição:{msg.description}, imagem:{msg.image_address}"}

@graph_router.delete("/delete")
async def delete_graph(name:dict):
   
    graphs = db.session.execute(select(Graph).where(Graph.name ==name["name"]))
    graph = [graph for graph in graphs][0][0]
    print("aaaaaa",graph)
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

