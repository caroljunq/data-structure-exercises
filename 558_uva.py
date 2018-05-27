# 558 Uva Challenge
from sys import maxsize as inf
n_case = int(input())
results = []

def bell_ford(graph, start):
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

while n_case > 0:
    n_case -= 1
    case_line = input()
    n,m = [int(x) for x in case_line.split(' ')]
    graph = {}

    for i in range(n):
        graph[i] = {}
    for _ in range(m):
        wormhole = input()
        x,y,t = [int(j) for j in wormhole.split(' ')]
        graph[x][y] = t

    neg_cycle = bell_ford(graph,x)
    travel_time = 'possible' if neg_cycle else 'not possible'
    results.append(travel_time)

for r in results:
    print(r)
