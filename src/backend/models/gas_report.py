from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from models.base import Base

class GasReport(Base):
    __tablename__ = "gas_report"
    id: Mapped[int] = mapped_column(primary_key=True)
    edge_id: Mapped[int] = mapped_column()#ForeignKey("edge_id")
    graph_id: Mapped[int] = mapped_column()#ForeignKey("graph_id")
    time: Mapped[str] = mapped_column()
    pression: Mapped[float] = mapped_column()

    def return_json(self):
        return {
            "id": self.id,
            "edge_id": self.edge_id,
            "graph_id": self.graph_id,
            "time": self.time,
            "pression": self.pression
        }