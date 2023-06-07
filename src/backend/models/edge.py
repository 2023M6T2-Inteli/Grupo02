from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from models.base import Base

class Edge(Base):
    __tablename__ = "edges"
    id: Mapped[int] = mapped_column(primary_key=True)
    weight: Mapped[float] = mapped_column()
    node1_id: Mapped[int] = mapped_column( nullable=False)#ForeignKey("node.id"),
    node2_id: Mapped[int] = mapped_column( nullable=False)#ForeignKey("node.id"),
    graph_id: Mapped[int] = mapped_column()#ForeignKey("graph.id")
    
    def return_json(self):

        return {
            "edge_id": self.id,
            "weight": self.weight,
            "from": self.node1_id,
            "target": self.node2_id,
            "graph_id": self.graph_id
            }
