from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.base import Base
from models.graph import Graph
from models.node import Node
from models.edge import Edge
from models.register import Register

engine = create_engine("sqlite+pysqlite:///models/data.db")
Base.metadata.create_all(engine)

session = Session(engine)
