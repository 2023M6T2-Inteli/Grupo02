from fastapi import APIRouter
from sqlalchemy import select
from config import db
from sqlalchemy import select
from models.graph import Graph
from config import db

graph_router = APIRouter(prefix='/graph')

@graph_router.get("/{type}/{val}")
async def get_graph(type,val):
    print("aaaaaaaaaaaaaa",type,val)
    if type == "id":
        stm = select(Graph).where(Graph.id ==val)
    if type == "name":
        stm = select(Graph).where(Graph.name ==val)
    graph = [graph for graph in db.session.execute(stm)][0][0]
    return graph.return_json()

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