# Dijkstra algorithm
from sys import maxsize as INF
import heapq

# Return the minimal distances from start to every node in graph
def dijks_distances(graph, start):
    queue = []
    distances = {}
    prev = {}
    for v in graph:
        distances[v] = INF
        prev[v] = None
        queue.append(v)

    distances[start] = 0
    while len(queue) > 0:
        dicio = {x:distances[x] for x in distances if x in queue}
        u = min(dicio, key=dicio.get) #select the min value
        queue.pop(queue.index(u))
        for v, w in graph[u]:
            alt = distances[u] + w
            if alt < distances[v]:
                distances[v] = alt
                prev[v] = u
    return distances, prev

# Return the path from start to end
def djks(graph, start, end):
    queue = []
    distances = {}
    prev = {}
    #stores the path from start to end
    path = [] #path is a stack
    #init all nodes with infinity and put into queue
    for v in graph:
        distances[v] = INF
        prev[v] = None
        queue.append(v)

    #define the start node as distance 0
    distances[start] = 0
    while len(queue) > 0:
        # select min distance in the queue
        dicio = {x:distances[x] for x in distances if x in queue}
        u = min(dicio, key=dicio.get)
        queue.pop(queue.index(u))
        #if end is hited
        if u == end:
            u = end
            while prev[u]:
                path.insert(0,u) #insert on top of the stack
                u = prev[u]
            path.insert(0,u)
            break #break if path is found
        #if path is not found, continues in the neighborhood
        for v, w in graph[u]:
            alt = distances[u] + w
            # the distances changes if a min value is found
            if alt < distances[v]:
                distances[v] = alt
                prev[v] = u
    # return [] is case of there is no path between start and end nodes
    return path if len(path) >= 2 else []

# relax( Node u, Node v, double w[][] )
#     if d[v] > d[u] + w[u,v] then
#        d[v] := d[u] + w[u,v]
#        pi[v] := u
# The algorithm itself is now:
# shortest_paths( Graph g, Node s )
#     initialise_single_source( g, s )
#     S := { 0 }        /* Make S empty */
#     Q := Vertices( g ) /* Put the vertices in a PQ */
#     while not Empty(Q)
#         u := ExtractCheapest( Q );
#         AddNode( S, u ); /* Add u to S */
#         for each vertex v in Adjacent( u )
#             relax( u, v, w )

# Dijkstra Algorithm with Priority Queue
#Input # graph = {
#     'a': {'b': 1}
# }
def dijkstra_pq(graph, start, goal):
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

# graph = {
#   'Home': [('A',3),('B',2),('C',5)],
#   'A': [('D',3),('Home',3)],
#   'B': [('D',1),('Home',2),('E',6)],
#   'C': [('E',2),('Home',5)],
#   'D': [('A',3),('B',1),('F',4)],
#   'E': [('B',6),('C',2),('School',4),('F',1)],
#   'F': [('D',4),('E',1),('School',2)],
#   'School': [('E',4),('F',2)]
# }
#
# print(djks(graph,'Home','School'))

graph = {
    'a': [('b',2),('c',4)],
    'b': [('a',2),('c',1),('d',4),('e',2)],
    'c': [('a',4),('e',3),('b',1)],
    'd': [('b',4),('e',3),('f',2)],
    'e': [('d',3),('b',2),('f',2),('c',3)],
    'f': [('d',2),('e',2)]
}
#
# print(dijks_distances(graph,'a'))

# se não tiver caminho, retorna só uma array com o elemento final
# graph = {
#     'a': [('b',0)],
#     'b': [],
#     'c':[]
# }
#
graph = {
    'a': {'b':2,'c':4},
    'b': {'a':2,'c':1,'d':4,'e':2},
    'c': {'a':4,'e':3,'b':1},
    'd': {'b':4,'e':3,'f':2},
    'e': {'d':3,'b':2,'f':2,'c':3},
    'f': {'d':2,'e':2}
}

print(dijkstra_pq(graph,'a','f'))
