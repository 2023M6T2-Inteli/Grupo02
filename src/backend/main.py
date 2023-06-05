from fastapi import FastAPI
from pydantic import BaseModel
from models import Membro
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()

engine = create_engine("sqlite+pysqlite:///models/data.db")
Base.metadata.create_all(engine)

app = FastAPI()

class Member(BaseModel):
    name: str
    description: str | None = None
    age: int
    feliz: bool | None = None

@app.get("/")
async def root():
    return {"message": "Hello, world!"}

@app.get("/item/{item_maneiro}")
async def read_item(item_maneiro: str):
    return {"item_maneiro": item_maneiro}

@app.post("/")
async def post_root(message: Member):
    return "Membro: " + str(message.id) + " " + str(message.name) + " " + str(message.age) + " " + str(message.feliz) + " " + str(message.description) + ""

@app.post("/criar_membro")
async def post_root(message: Member):
    session = Session(engine)
    membro = Membro(name = message.name, description = message.description, age = message.age, feliz = message.feliz)
    session.add(membro)
    session.commit()
    session.close()

    return f"nome:{message.name}, descrição:{message.description}, age:{message.age}, feliz:{message.feliz}"
