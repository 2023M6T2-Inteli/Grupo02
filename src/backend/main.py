from fastapi import FastAPI
from routes.node import node_router
from routes.graph import graph_router
from routes.edge import edge_router
from routes.image import router as image_router
from config import db

app = FastAPI()

db

app.include_router(node_router)
app.include_router(graph_router)
app.include_router(edge_router)
app.include_router(image_router)