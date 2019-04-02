def BFS1(graph,start):
    queue = [start]
    visited = [start]
    while queue:
        v = queue.pop(0)
        print(v)

        for u in graph[v]:
            if u not in visited:
                visited.append(u)
                queue.append(u)

def BFS_distance(graph,start):
    queue = [start]
    visited = [start]
    distances = {k: 0 for k in graph.keys()}
    while queue:
        v = queue.pop(0)
        for u,d in graph[v]:
            if u not in visited:
                visited.append(u)
                queue.append(u)
                distances[u] += distances[v] + d
    print(distances)

def dfs(graph, start, visited):
    visited.append(start)
    for v in graph[start]:
        if v not in visited:
            dfs(graph,v,visited)
    return visited

graph1 = {
    'A': ['B','S'],
    'B': ['A'],
    'C': ['S','D','E','F'],
    'D': ['C'],
    'E': ['C','H'],
    'F': ['C','G'],
    'G': ['F','H','S'],
    'H': ['E','G'],
    'S':['A','C','G']
}

# BFS1(graph1,'A')

graph2 = {
    'A': [('C',5),('B',5),('E',5)],
    'B': [('A',5),('D',3)],
    'C': [('A',5),('E',6),('D',4)],
    'D': [('B',3),('C',4)],
    'E': [('A',5),('C',6)],
}

graph3 = {
    'A': [('B',3)],
    'B': [('C',6),('D',1),('E',5)],
    'C': [('E',6)],
    'D': [('E',7)],
    'E': [],
}


BFS_distance(graph3,'A')
print(dfs(graph1,'A',[]))
