from fastapi import APIRouter
from sqlalchemy import select
from models.model_types import GraphT
from models.graph import Graph
from models.node import Node
from models.edge import Edge
from config import db
from math import sqrt

graph_router = APIRouter(prefix='/graph')


@graph_router.get("/get/{id}")
async def get_graph(id: int):
    stm = select(Graph).where(Graph.id == id)
    get_nodes = db.session.query(Node).filter(Node.graph_id == id).all()
    nodes = [nodes.return_json() for nodes in get_nodes]
    get_edges = db.session.query(Edge).filter(Edge.graph_id == id).all()
    edges = [edges.return_json() for edges in get_edges]

    for edge in edges:
        edge["from"] = {"x": nodes[edge["from"]]["x"],
                        "y": nodes[edge["from"]]["y"]}
        edge["target"] = {"x": nodes[edge["target"]]["x"],
                          "y": nodes[edge["target"]]["y"]}
    graph = [graph for graph in db.session.execute(stm)][0][0]

    graph_data = {
        "graph": graph.return_json(),
        "edges": [edge for edge in edges]
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
                x=round(edge['from']['x'],3),
                y=round(edge['from']['y'],3),
                first_node=False,
                graph_id=graph.id

            )
            if node1 not in nodes:
                nodes.append(node1)

            node2 = Node(
                x=edge['to']['x'],
                y=edge['to']['y'],
                first_node=False ,
                graph_id=graph.id

            )

            if node2 not in nodes:
                nodes.append(node2)
            
        db.session.add_all(nodes)
        db.session.commit()
                    
        nodes = db.session.query(Node).filter(Node.graph_id == graph.id).all()
        for node in nodes:
            print(node.id)

        for edge in msg.edges:
            node1 = db.session.query(Node).filter(Node.x == round(edge['from']['x'], 3) and Node.y == round(edge['from']['y'], 3) and Node.graph_id == graph.id).first()
            node2 = db.session.query(Node).filter(Node.x == round(edge['to']['x'], 3) and Node.y == round(edge['to']['y'], 3) and Node.graph_id == graph.id).first()
            weight = sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)
            print("weight: ", weight)
            edge_ = Edge(
                weight=weight,
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
async def delete_graph(name: dict):

    graphs = db.session.execute(
        select(Graph).where(Graph.name == name["name"]))
    graph = [graph for graph in graphs][0][0]
    db.session.delete(graph)
    db.session.commit()

    return {'success': f'Graph {name["name"]} was successfully deleted'}


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
