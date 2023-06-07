from fastapi import APIRouter
from sqlalchemy import select
from models.model_types import NodeT
from models.node import Node
from models.edge import Edge
from config import db
from sqlalchemy import or_
node_router = APIRouter(prefix="/node")

@node_router.get("/get/{id}")
async def get_node(id: int):
    node = db.session.query(Node).filter(Node.id == id).first()
    
    return {node}

@node_router.post("/create")
async def create_nodes(msg: NodeT):
    
    node = Node(x = msg.x,
                y = msg.y,
                first_node = msg.first_node,
                graph_id = msg.graph_id)
    
    db.session.add(node)
    db.session.commit()

    return f"Node created with values x={msg.x}, y={msg.y}, first_node={msg.first_node}, graph_id={msg.graph_id}"

@node_router.delete('/delete/{id}')
async def delete_node(id: int):

    node = db.session.execute(select(Node).where(Node.id == id))
    edges1 = db.session.query(Edge).filter(Edge.node1_id == id).all()
    edges2 = db.session.query(Edge).filter(Edge.node2_id == id).all()
    
    for edge in edges1:
        db.session.delete(edge)
        
    for edge in edges2:
        db.session.delete(edge)

    stm = select(Node).where(Node.id == id)
    node = [node for node in db.session.execute(stm)][0][0]

    
    db.session.delete(node)
    db.session.commit()
    return {'success': f"deleted node with id {id}"}