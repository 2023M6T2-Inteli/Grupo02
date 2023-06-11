from pydantic import BaseModel

class NodeT(BaseModel):
    x: float
    y: float
    first_node: bool 
    graph_id: int

class EdgeT(BaseModel):
    weight: float
    nodes: list
    graph_id: int

class GraphT(BaseModel):
    id: int | None = None
    name: str
    description: str | None = None
    image_address: str | None = None

class RegisterT(BaseModel):
    graph_id: int
    date: str | None = None
    name: str
    description: str | None = None