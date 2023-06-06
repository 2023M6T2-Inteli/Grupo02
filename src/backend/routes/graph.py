from fastapi import APIRouter
from sqlalchemy import select
from models.model_types import GraphT 
from models.graph import Graph
from engine import engine, session

graph_router = APIRouter(prefix='/graph')

@graph_router.get("/")
async def get_graph(id:int):

    print(select(Graph).where(Graph.id == id))
    # return {"id":}

@graph_router.post("/create_graph")
async def post_root(msg: GraphT):
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa", msg)
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa", msg.name)
    
    graph = Graph(name = msg.name,
                  description = msg.description,
                  image_address = msg.image_address)

    session.add(graph)
    session.commit()
    session.close()

    return {f"nome:{msg.name}, descrição:{msg.description}, imagem:{msg.image_address}"}
