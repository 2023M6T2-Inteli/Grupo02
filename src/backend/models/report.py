from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from models.base import Base

class Report(Base):
    __tablename__ = "report"
    id: Mapped[int] = mapped_column(primary_key=True)
    graph_id: Mapped[int] = mapped_column()#ForeignKey("graph_id")
    gas_report_id: Mapped[int] = mapped_column()#ForeignKey("gas_report_id")
    date: Mapped[str] = mapped_column()
    images_report_id: Mapped[int] = mapped_column()#ForeignKey("images_report_id")

    def return_json(self):

        return {
            "report_id": self.id,
            "sensors": self.sensors,
            "date": self.date,
            "images_report_id": self.images_report_id
        }