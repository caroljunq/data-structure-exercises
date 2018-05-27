# Bellman Ford Algorithm
from sys import maxsize as inf

def bell_ford(graph, start):
    distances = {}
    prev = {}
    negative = False

    for v in graph:
        prev[v] = None
        if v == start:
            distances[v] = 0
        else:
            distances[v] = inf

    for _ in range(0, len(graph) - 1):
        for u in graph:
            for v,w in graph[u]:
                if distances[u] != inf:
                    if (distances[u] + w) < distances[v]:
                        distances[v] = distances[u] + w
                        prev[v] = u

    #checking for negative, if is true, set the new distance as INFINITY
    # for _ in range(0, len(graph) - 1):
    for u in graph:
        for v, w in graph[u]:
            if (distances[u] + w) < distances[v]:
                print("há negativo")
                negative = True
                # distances[u] = inf
                # negative = True // in case of negative cycles
                # do something if there is a negative cycle

    return distances,prev,negative

# return the shortest path between 2 nodes
# if there is no path, return []
def bell_ford_between(graph, start, end):
    d, prev, neg = bell_ford(graph, start)
    path = []
    for u in graph:
        if u == end:
            u = end
            while prev[u] and neg == False: #SE PRECISAR para parar quando há negativo
            # while prev[u]:
                path.insert(0,u) #insert on top of the stack
                u = prev[u]
            path.insert(0,u)

    return path if len(path) >= 2 else []

def bell_ford222C(graph, start):
    distances = {x:inf for x in graph.keys()}
    distances[start] = 0
    negative = False

    for _ in range(0, len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                w = graph[u][v]
                if (distances[u] + w) < distances[v]:
                    distances[v] = distances[u] + w

    for u in graph:
        for v in graph[u]:
            w = graph[u][v]
            if (distances[u] + w) < distances[v]:
                negative = True
    return negative
# graph = {
#     '1': [('3',6),('4',3)],
#     '2': [('1',3)],
#     '3': [('4',2)],
#     '4': [('3',1),('2',1)],
#     '5': [('2',4),('4',2)]
# }

# graph = {
#     'S': [('E',8),('A',10)],
#     'A': [('C',2)],
#     'B': [('A',1)],
#     'C': [('B',-2)],
#     'D': [('C',-1),('A',-4)],
#     'E': [('D',1)]
# }

# graph = {
#     'A': [('B',4),('C',2)],
#     'B': [('C',3),('D',2),('E',3)],
#     'C': [('B',1),('D',4),('E',5)],
#     'D': [],
#     'E': [('D',-5)]
# }

# Nesse aqui há ciclo negativo
# graph = {
#     '0': [('1',5),('2',4)],
#     '1': [('3',3)],
#     '2': [('1',-6)],
#     '3': [('2',2)]
# }

# graph = {
#     '0': [('1',5),('2',2)],
#     '1': [('3',4),('1',3)],
#     '2': [('3',6)],
#     '3': [('0',-1)]
# }

graph = {
    'S': [('A',5),('C',-2)],
    'A': [('B',1)],
    'B': [('C',2),('D',7),('t',3)],
    'C': [('A',2),('D',3)],
    'D': [('t',10)],
    't': []
}

print(bell_ford_between(graph,'S','D'))
