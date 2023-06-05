from base import Base
from sqlalchemy import create_engine
from graph import Graph
from node import Node
from edge import Edge

if __name__ == "__main__":

    engine = create_engine("sqlite+pysqlite:///data.db")
    Base.metadata.create_all(engine)