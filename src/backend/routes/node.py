from fastapi import APIRouter
from models.node import Node
from models.model_types import Node as node_type
from sqlalchemy import create_engine
from engine import engine, session

router = APIRouter(prefix="/node")

@router.post("/node")
async def create_nodes(json: node_type):
    x = json.x
    y = json.y
    first_node = json.first_node
    graph_id = json.graph_id

    node = Node(x=x, y=y, first_node=first_node, graph_id=graph_id)

    session.add(node)
    session.commit()

    return f"Node created with values x={x}, y={y}, first_node={first_node}, graph_id={graph_id}"