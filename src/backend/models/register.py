from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, DateTime
from models.base import Base

class Register(Base):
    __tablename__= "register"
    id: Mapped[int] = mapped_column(primary_key=True)
    graph_id: Mapped[int] = mapped_column()#ForeignKey("graph_id")
    date: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

    def return_json(self):

        return {
            "id": self.id,
            "name": self.name,
            "graph_id": self.graph_id,
            "date": self.date,
            "description": self.description
        }