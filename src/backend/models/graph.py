from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from models.base import Base

class Graph(Base):
    __tablename__ = "graph"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String())
    image_address: Mapped[str] = mapped_column(String(),nullable=False)
    
    def return_json(self):

        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "image_address": self.image_address,
            }
