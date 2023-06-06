from fastapi import FastAPI
from routes.node import router as node_router
from routes.graph import graph_router

app = FastAPI()

app.include_router(node_router)
app.include_router(graph_router)
