from fastapi import FastAPI
from routes.node import node_router
from routes.graph import graph_router
from routes.edge import edge_router
from routes.image import image_router
from routes.register import register_router
from config import db
#cors
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI( )

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://localhost:8000",
    "localhost:8000",
    "http://localhost:8080",
    "localhost:8080"]
db

app.add_middleware( 
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(node_router)
app.include_router(graph_router)
app.include_router(edge_router)
app.include_router(image_router)
app.include_router(register_router)