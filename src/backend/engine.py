from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()

engine = create_engine("sqlite+pysqlite:///models/data.db")
Base.metadata.create_all(engine)

session = Session(engine)