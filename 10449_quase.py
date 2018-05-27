from sys import maxsize as inf

n_case = 0

def bell_ford(graph, start):
    distances = {x:inf for x in graph.keys()}
    distances[start] = 0
    negative = False

    for _ in range(0, len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                w = graph[u][v]
                if (distances[u] + w) < distances[v] and distances[u] != inf:
                    distances[v] = distances[u] + w

    for u in graph:
        for v in graph[u]:
            w = graph[u][v]
            if distances[u] + w < distances[v]:
                distances[u] = inf
                distances[v] = inf
    return distances

while True:
    graph = {}
    costs = []
    try:
        case_line = input()
    except EOFError:
        break
    if case_line == '':
        break
    busyness_info = [int(x) for x in case_line.split(' ')]
    n_junc = busyness_info[0]
    for i in range(1, len(busyness_info)):
        graph[i] = {}
        costs.append(busyness_info[i])
    n_roads = int(input())
    for _ in range(n_roads):
        src,dest = [int(x) for x in input().split(' ')]
        graph[src][dest] = (costs[dest - 1] - costs[src - 1]) ** 3

    n_queries = int(input())
    answer = []
    for _ in range(n_queries):
        dt = int(input())
        d = bell_ford(graph,1)
        answer.append('?' if d[dt] < 3  or d[dt] >= inf  else d[dt])
    n_case += 1
    print('Set #'+ str(n_case))
    for el in answer:
        print(el)
