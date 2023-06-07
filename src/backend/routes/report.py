from fastapi import APIRouter
from sqlalchemy import select
from models.report import Report
from models.model_types import ReportT
from config import db
from datetime import datetime

report_router = APIRouter(prefix='/report')

# @report_router.get("/{type}/{val}")
# async def get_graph(type,val):
#     print("aaaaaaaaaaaaaa",type,val)
#     if type == "id":
#         stm = select(Graph).where(Graph.id ==val)
#     if type == "name":
#         stm = select(Graph).where(Graph.name ==val)
#     graph = [graph for graph in db.session.execute(stm)][0][0]
#     return graph.return_json()


@report_router.post("/create")
async def post_root(msg: ReportT):
    date = datetime.now()
    report = Report(graph_id = msg.graph_id,
                    gas_report_id = msg.gas_report_id,
                    date = str(date),
                    images_report_id = msg.images_report_id)

    db.session.add(report)
    db.session.commit()
    db.session.close()
    
    return  {f"eu sou idiota"}

@report_router.delete("/delete")
async def delete_graph(name:dict):
   
    graphs = db.session.execute(select(Graph).where(Graph.name ==name["name"]))
    graph = [graph for graph in graphs][0][0]
    print("aaaaaa",graph)
    db.session.delete(graph)
    db.session.commit()

@report_router.put("/update")
async def update_graph(json:dict):
    graph = [graph for graph in db.session.execute(select(Graph).where(Graph.id == json["id"]))][0][0]
    for key in json.keys():
        if key == "name":
            graph.name = json["name"]
        elif key == "description":
            graph.description = json["description"]
        elif key == "image_address":
            graph.image_address = json["image_address"]
    db.session.commit()


    return {"eu sou otario"}
