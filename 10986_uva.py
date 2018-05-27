# 10986 UVa

from sys import maxsize as INF
import heapq

def dijkstra(graph, start, goal):
    distances = {x: INF for x in graph.keys()}
    visited = []
    distances[start] = 0
    pq = [(0,start)]
    while pq:
        d,u = heapq.heappop(pq)
        visited.append(u)
        for v in graph[u]:
            w = graph[u][v]
            if v not in visited and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                heapq.heappush(pq,(distances[v],v))
    return distances[goal]

N = int(input())
n_case = 0
results = []

# count number of cases
while n_case < N:
    case_line = input()
    n,m,s,t = [int(x) for x in case_line.split(' ')]
    n_case += 1
    graph = {}

    for i in range(n):
        graph[i] = {}
    for _ in range(m):
        cable_line = input()
        s1,s2,w = [int(x) for x in cable_line.split(' ')]
        if s1 not in graph[s2].keys():
            graph[s2][s1] = w
        else:
            if w < graph[s2][s1]:
                graph[s2][s1] = w
        if s2 not in graph[s1].keys():
            graph[s1][s2] = w
        else:
            if w < graph[s1][s2]:
                graph[s1][s2] = w

    result = dijkstra_pq(graph, s,t)
    miliseconds = result if result != INF else 'unreachable'
    results.append('Case #'+str(n_case)+": "+str(miliseconds))

for r in results:
    print(r)
