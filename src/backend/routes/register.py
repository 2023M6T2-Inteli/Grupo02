from fastapi import APIRouter
from sqlalchemy import select
from models.model_types import RegisterT
from models.register import Register
from config import db
from datetime import datetime

register_router = APIRouter(prefix="/register")

@register_router.get("/{type}/{val}")
async def get_register(type,val):
    if type == "id":
        stm = select(Register).where(Register.id == val)
    if type == "register_name":
        stm = select(Register).where(Register.name == val)
    else:
        print(stm)
    register = [register for register in db.session.execute(stm)][0][0]
    return register.return_json()

@register_router.get("/get_all")
async def get_register():
    registers = db.session.query(Register).order_by(Register.date).all()
    registers_data = [reg.return_json() for reg in registers]
    return registers_data
    
@register_router.delete("/delete")
async def delete_graph(msg:dict):
   
    registers = db.session.execute(select(Register).where(Register.name == msg["name"]))
    register = [reg for reg in registers][0][0]

    db.session.delete(register)
    db.session.commit()

@register_router.post("/create")
async def get_register(msg: RegisterT):
    date = datetime.now()
    register = Register(
        graph_id = msg.graph_id,
        date = date,
        name = msg.name,
        description = msg.description)

    db.session.add(register)
    db.session.commit()
    db.session.close()

    return f"Register created with values graph_id={msg.graph_id}, date={msg.date}, register_name={msg.name}, description={msg.description}"