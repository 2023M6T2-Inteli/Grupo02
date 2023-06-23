from fastapi import APIRouter
from sqlalchemy import select
from models.model_types import GraphT
from models.graph import Graph
from models.node import Node
from models.edge import Edge
from config import db
from math import sqrt
import json

graph_router = APIRouter(prefix='/graph')


@graph_router.get("/get/{id}")
async def get_graph(id: int):
    stm = select(Graph).where(Graph.id == id)
    get_edges = db.session.query(Edge).filter(Edge.graph_id == id).all()
    edges = [edges.return_json() for edges in get_edges]

    for edge in edges:
        edge["from"] = {"x": (((db.session.query(Node).filter(Node.id == edge["from"])).first()).return_json())["x"],
                        "y": (((db.session.query(Node).filter(Node.id == edge["from"])).first()).return_json())["y"]}

        edge["target"] = {"x": (((db.session.query(Node).filter(Node.id == edge["target"])).first()).return_json())["x"],
                          "y": (((db.session.query(Node).filter(Node.id == edge["target"])).first()).return_json())["y"]}

    graph = [graph for graph in db.session.execute(stm)][0][0]

    graph_data = {
        "graph": graph.return_json(),
        "edges": [edge for edge in edges],
    }

    return graph_data


@graph_router.get("/get_gazebo/{id}")
async def get_graph(id: int):
    stm = select(Graph).where(Graph.id == id)
    nodes = db.session.query(Node).filter(Node.graph_id == id).all()
    edges = db.session.query(Edge).filter(Edge.graph_id == id).all()
    graph = [graph for graph in db.session.execute(stm)][0][0]

    graph_data = {
        "graph": graph.return_json(),
        "nodes": [node.return_json() for node in nodes],
        "edges": [edge.return_json() for edge in edges],
    }


    return graph_data


@graph_router.get("/get_all")
async def get_graphs():
    graphs = db.session.query(Graph).all()
    graph_data = [graph.return_json() for graph in graphs]
    for graph in graph_data:
        nodes = db.session.query(Node).filter(
            Node.graph_id == graph['id']).all()
        edges = db.session.query(Edge).filter(
            Edge.graph_id == graph['id']).all()

        graph['nodes'] = [node.return_json() for node in nodes]
        graph['edges'] = [edge.return_json() for edge in edges]

    return graph_data


@graph_router.post("/create")
async def post_root(msg: GraphT):
    try:
        graphs = db.session.query(Graph).all()

        # Verificação de nó igual
        graph_data = [(graph.return_json()) for graph in graphs]
        for content in graph_data:
            if content["name"] == msg.name:
                return "Nome já cadastrado"

        graph = Graph(name=msg.name,
                      description=msg.description,
                      image_address=msg.image_address)

        db.session.add(graph)
        db.session.commit()

        graph = db.session.query(Graph).filter(Graph.name == msg.name).first()

        nodes = []
        for edge in msg.edges:
            node1 = Node(
                x=round(edge['from']['x'], 3),
                y=round(edge['from']['y'], 3),
                first_node=False,
                graph_id=graph.id

            )

            node2 = Node(
                x=round(edge['to']['x'], 3),
                y=round(edge['to']['y'], 3),
                first_node=False,
                graph_id=graph.id

            )

            if nodes != []:
                i = 0
                for node in nodes:
                    i += 1
                    if node.x == node1.x and node.y == node1.y:
                        break
                    if i == len(nodes):
                        nodes.append(node1)
                i = 0
                for node in nodes:
                    i += 1
                    if node.x == node2.x and node.y == node2.y:
                        break
                    if i == len(nodes):
                        nodes.append(node2)
            else:
                nodes.append(node1)
                nodes.append(node2)

        db.session.add_all(nodes)
        db.session.commit()

        nodes = db.session.query(Node).filter(Node.graph_id == graph.id).all()
        for node in nodes:
            print(node.id)

        for edge in msg.edges:

            node1 = db.session.query(Node).filter(Node.x == round(edge['from']['x'], 3) and Node.y == round(
                edge['from']['y'], 3) and Node.graph_id == graph.id).first()
            node2 = db.session.query(Node).filter(Node.x == round(edge['to']['x'], 3) and Node.y == round(
                edge['to']['y'], 3) and Node.graph_id == graph.id).first()
            print(f"---- N1: {node1.id}       N2: {node2.id}")
            weight = sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)
            edge_ = Edge(
                weight=round(weight, 3),
                node1_id=node1.id,
                node2_id=node2.id,
                graph_id=graph.id
            )
            db.session.add(edge_)

        db.session.commit()
        print("Salve -------------------------------------")

        db.session.close()

        return {f"Sucessful create graph {msg.name}"}
    except Exception as e:
        return {'erro': str(e)}


@graph_router.delete("/delete")
async def delete_graph(name_: dict):
    graphs = db.session.execute(
        select(Graph).where(Graph.name == name_["name"]))
    graph = [graph for graph in graphs][0][0]
    db.session.delete(graph)
    # db.session.commit()
    G_id = graph.return_json()["id"]
    edges = db.session.query(Edge).filter(Edge.graph_id == G_id).all()

    for edge in edges:
        db.session.delete(edge)

    nodes = db.session.query(Node).filter(Node.graph_id == G_id).all()

    for node in nodes:
        db.session.delete(node)

    db.session.commit()

    return {'success': f'Graph {name_["name"]} was successfully deleted'}


@graph_router.put("/update")
async def update_graph(json: dict):
    graph = [graph for graph in db.session.execute(
        select(Graph).where(Graph.id == json["id"]))][0][0]
    for key in json.keys():
        if key == "name":
            graph.name = json["name"]
        elif key == "description":
            graph.description = json["description"]
        elif key == "image_address":
            graph.image_address = json["image_address"]
    db.session.commit()

    return {'success': 'Graph successfully updated'}
