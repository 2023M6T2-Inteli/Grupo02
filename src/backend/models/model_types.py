from pydantic import BaseModel
from sqlalchemy import DateTime

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
    id: int | None = None
    name: str
    description: str | None = None
    image_address: str | None = None

class ReportT(BaseModel):
    graph_id: int
    report_id: int
    date: DateTime

class HistoryT(BaseModel):
    id: int | None = None
    graph_id: int
    report_id: int
    data: DateTime| None = None
    history_name: str
    description: str | None = None 


    id: Mapped[int] = mapped_column(primary_key=True)
    graph_id: Mapped[int] = mapped_column(ForeignKey("graph_id"))
    report_id: Mapped[int] = mapped_column(ForeignKey("report_id"))
    date: Mapped[DateTime] = mapped_column()
    history_name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()