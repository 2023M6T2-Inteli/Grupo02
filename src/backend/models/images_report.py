from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base

class Images(Base):
    __tablename__ = "images_report"
    id: Mapped[int] = mapped_column(primary_key=True)
    edge_id: Mapped[int] = mapped_column()#ForeignKey("edge_id")
    graph_id: Mapped[int] = mapped_column()#ForeignKey("graph.id")
    time: Mapped[str] = mapped_column()
    address: Mapped[str] = mapped_column()

    def return_json(self):

        return {
            "images_report_id": self.id,
            "edge_id": self.edge_id,
            "graph_id": self.graph_id,
            "time": self.time,
            "address": self.address
        }