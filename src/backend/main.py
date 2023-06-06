from fastapi import FastAPI
from routes.node import router as node_router
from routes.graph import graph_router
from config import db

app = FastAPI()

db

app.include_router(node_router)
app.include_router(graph_router)
