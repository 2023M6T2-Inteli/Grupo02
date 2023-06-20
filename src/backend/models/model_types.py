from pydantic import BaseModel

class NodeT(BaseModel):
    x: float
    y: float
    first_node: bool 
    graph_id: int

class EdgeT(BaseModel):
    weight: float
    node1_id: int
    node2_id: int
    graph_id: int

class GraphT(BaseModel):
    name: str
    description: str | None = None
    image_address: str | None = None
    edge: list | None = None

class RegisterT(BaseModel):
    graph_id: int
    date: str | None = None
    name: str
    description: str | None = None
    
class ImageT(BaseException):
    graph_id: int
    edge_id: int
    time: str
    address: str