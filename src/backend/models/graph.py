from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String
from base import Base

class Graph(Base):
    __tablename__ = "graph"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    description: Mapped[str] = mapped_column()
    image_address: Mapped[str] = mapped_column(nullable=False)
    
    def return_json(self):

        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "image": self.image_address,
            }
