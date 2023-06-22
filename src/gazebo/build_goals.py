import requests
import networkx as nx
from networkx.algorithms.approximation import traveling_salesman_problem as tsp


def request(graph_id: int):
    data = requests.get(f'http://localhost:8000/graph/get_gazebo/{graph_id}')
    nodes = data.json()['nodes']
    edges = data.json()['edges']
    return nodes, edges

# Build the graph


def build_graph(graph_id: int):
    nodes, edges = request(graph_id)
    graph = {}
    for node in nodes:
        edge_in_node = {}
        for edge in edges:
            if edge['target'] == node['id'] or edge['from'] == node['id']:
                edge_in_node[(edge['target'] if edge['from'] == node['id'] else edge['from'])] = {
                    'weight': edge['weight']}

        graph[node['id']] = edge_in_node
    return graph, nodes


def build_goals(graph_id: int):
    graph, nodes = build_graph(graph_id)
    goals = []

    for node_id in tsp(nx.Graph(graph)):
        for node in nodes:
            if node['id'] == node_id:
                goals.append((node['x'], node['y']))
                break
    print("Goals: ", goals)
    return goals
