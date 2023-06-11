from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import ForeignKey
from models.base import Base
from typing import List



class Node(Base):
    __tablename__ = "node"
    id: Mapped[int] = mapped_column(primary_key=True)
    x: Mapped[float] = mapped_column()
    y: Mapped[float] = mapped_column()
    first_node: Mapped[bool] = mapped_column()
    graph_id: Mapped[int] = mapped_column()#ForeignKey("graph.id")
    edge_id: Mapped[int] = mapped_column(ForeignKey("edge.id"))
    edge: Mapped["Edge"] = relationship(back_populates="nodes")
    
    def return_json(self):

        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "first_node": self.first_node,
            "graph_id": self.graph_id,
            }
        
    def __repr__(self):
        return f"Node(id={self.id}, x={self.x}, y={self.y}, first_node={self.first_node}, graph_id={self.graph_id})"


class Edge(Base):
    __tablename__ = "edges"
    id: Mapped[int] = mapped_column(primary_key=True)
    weight: Mapped[float] = mapped_column()
    nodes: Mapped[List["Node"]] = relationship(
         back_populates="edge", cascade="all, delete-orphan"
     )
    graph_id: Mapped[int] = mapped_column()#ForeignKey("graph.id")
    
    def return_json(self):

        return {
            "edge_id": self.id,
            "weight": self.weight,
            "nodes":self.nodes,
            "graph_id": self.graph_id
            }
