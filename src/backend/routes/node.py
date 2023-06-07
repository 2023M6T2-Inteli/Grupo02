from fastapi import APIRouter
from sqlalchemy import select
from models.model_types import NodeT
from models.node import Node
from config import db

node_router = APIRouter(prefix="/node")

@node_router.post("/create")
async def create_nodes(msg: NodeT):
    
    node = Node(x = msg.x,
                y = msg.y,
                first_node = msg.first_node,
                graph_id = msg.graph_id)
    
    db.session.add(node)
    db.session.commit()

    return f"Node created with values x={msg.x}, y={msg.y}, first_node={msg.first_node}, graph_id={msg.graph_id}"

@node_router.delete('/delete')
async def delete_node(node: dict):
    # para deletar um nó, também preciso deletar todas as arestas com o id dele, dessa forma:
    
    # deleta o nó
    dNode = db.session.execute(select(Node).where(Node.id == node['id']))
    stm = select(Node).where(Node.id == node['id'])
    node = [node for node in db.session.execute(stm)][0][0]
    node_id = node['id']
    
    db.session.delete(dNode)
    db.session.commit()
    return 
    # para cada aresta que possua o id do nó que deleite,
    
        #deleta a aresta
    