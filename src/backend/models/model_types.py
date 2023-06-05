from pydantic import BaseModel

class Node(BaseModel):
    x: float
    y: float
    first_node: bool 
    graph_id: int

class Edge(BaseModel):
    weight: float
    node1_id: int
    node2_id: int
    graph_id: int

class Graph(BaseModel):
    name: str
    description: str | None = None
    image_address: str | None = None