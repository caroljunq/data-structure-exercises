# Floyad Warshall
from sys import maxsize as inf

def floyd_warshall(graph):
    distances = init_graph(graph)
    keys = graph.keys()
    pred = {}

    for v in graph:
        pred[v] = {}
        for k in keys:
            if k == v:
                pred[v][k] = 0
            else:
                pred[v][k] = k

    for k in keys:
        for i in keys:
            for j in keys:
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k]+distances[k][j]
                    pred[i][j] = pred[i][k]
    return distances,pred

def init_graph(graph):
    keys = graph.keys()
    for k in keys:
        for v in graph:
            if k not in graph[v]:
                graph[v][k] = inf
            if k == v:
                graph[v][v] = 0
    return graph

# return the path between two vertices
def paths(graph, start, end):
    d, prev = floyd_warshall(graph)
    path = [start]
    if prev[start][end] == None:
        return []

    while start != end:
       start = prev[start][end]
       path.append(start)
    return path


# graph = {
#     '1':{'3':6,'4':3},
#     '2':{'1': 3},
#     '3':{'4':2},
#     '4':{'3':1, '2':1},
#     '5':{'2':4,'4':2}
# }

# graph = {
#     '1':{'3':-2},
#     '2':{'1': 4, '3':3},
#     '3':{'4':2},
#     '4':{'2': -1}
# }

graph = {
    '1':{'3':-2},
    '2':{'1': 4, '3':3},
    '3':{'4':2},
    '4':{'2': -1}
}

# graph = {
#     '1': {'2': 5, '4': 2,'3':1},
#     '2': {'3':3, '1':5},
#     '3': {'2':3,'1':1,'4':4},
#     '4': {'1':2, '3':4}
# }

print(paths(graph, '3', '1'))
