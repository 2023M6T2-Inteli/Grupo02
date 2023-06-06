from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, DateTime
from models.base import Base

class History(Base):
    __tablename__: "history"
    id: Mapped[int] = mapped_column(primary_key=True)
    graph_id: Mapped[int] = mapped_column(ForeignKey("graph_id"))
    report_id: Mapped[int] = mapped_column(ForeignKey("report_id"))
    date: Mapped[DateTime] = mapped_column()
    history_name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

    def return_json(self):

        return {
            "history_id": self.id,
            "graph_id": self.graph_id,
            "report_id": self.report_id,
            "date": self.date,
            "history_name": self.history_name,
            "description": self.description
        }