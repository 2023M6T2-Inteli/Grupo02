from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, DateTime
from models.base import Base

class Register(Base):
    __tablename__= "register"
    id: Mapped[int] = mapped_column(primary_key=True)
    graph_id: Mapped[int] = mapped_column()#ForeignKey("graph_id")
    report_id: Mapped[int] = mapped_column()#ForeignKey("report_id")
    date: Mapped[str] = mapped_column()
    register_name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

    def return_json(self):

        return {
            "register_id": self.id,
            "graph_id": self.graph_id,
            "report_id": self.report_id,
            "date": self.date,
            "register_name": self.register_name,
            "description": self.description
        }