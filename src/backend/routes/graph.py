from fastapi import APIRouter
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
# from models.model_types import Graph 
from models.graph import Graph
from pydantic import BaseModel

class GraphT(BaseModel):
    name: str
    description: str 
    image_address: str

graph_router = APIRouter(prefix='/graph')

engine = create_engine("sqlite+pysqlite:///../data.db")

@graph_router.get("/")
async def get_graph(id:int):
    session = Session(engine)
    print(select(Graph).where(Graph.id == id))
    # return {"id":}

@graph_router.post("/create_graph")
async def post_root(msg: GraphT):
    session = Session(engine)
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa", msg)
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa", msg.name)
    
    graph = Graph(name = msg.name,
                  description = msg.description,
                  image_address = msg.image_address)

    session.add(graph)
    session.commit()
    session.close()

    return {f"nome:{msg.name}, descrição:{msg.description}, imagem:{msg.image_address}"}
