import networkx as nx
import math
from networkx.algorithms.approximation import traveling_salesman_problem

goals = {'a': (1.0, 2.0), # 'a'
         'b': (4.0, 5.0), # 'b'
         'c': (2.0, 1.0), # 'c'
         'd': (3.0, 3.0), # 'd'
         'e': (5.0, 1.0), # 'e'
         'f': (5.0, 4.0), # 'f'
         'g': (7.0, 8.0), # 'g'
         'h': (0.0, 0.0)} # 'h'

G = nx.Graph()
i = 0
for goal in goals:
    G.add_node(goal)
    for edge in goals:
        G.add_edge(goal, edge, weight=math.dist(goals[goal], goals[edge]))
print(G.adj)

print('\n'*3)
tsp = traveling_salesman_problem
print(tsp(G, nodes=['a', 'g', 'b', 'f']))
