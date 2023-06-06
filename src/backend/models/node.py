# Estrutura das tabelas que temos no banco de dados

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from models.base import Base

class Node(Base):
    __tablename__ = "node"
    id: Mapped[int] = mapped_column(primary_key=True)
    x: Mapped[float] = mapped_column()
    y: Mapped[float] = mapped_column()
    first_node: Mapped[bool] = mapped_column()
    graph_id: Mapped[int] = mapped_column(ForeignKey("graph.id"))
    
    def return_json(self):

        return {
            "node_id": self.id,
            "x": self.x,
            "y": self.y,
            "first_node": self.first_node,
            "graph_id": self.graph_id,
            }

