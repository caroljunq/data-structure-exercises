# UVA 11060
# priority queue and methods
from heapq import heappush, heappop

# Topological Sort through Kahn Sort
def kahn_sort(graph):
    #list with sorted nodes
    sorted_list = []
    #nodes without incoming edges, priority queue
    no_incoming = []
    #stores in_degree for each node
    in_degree = {v: 0 for v in graph.keys()}


    # for u in graph:
    #     in_degree[u] = 0
    #     for v in graph:
    #         # get all elements except first (insertion index)
    #         if u in graph[v][1:]:
    #             in_degree[u] += 1

    # count incoming edges for each node
    for adj in graph.values():
        for v in adj[1:]:
            in_degree[v] += 1

    # select all nodes with 0 incoming edges
    for v in graph:
        if in_degree[v] == 0:
            heappush(no_incoming,(graph[v][0],v))

    # goes through graph to find the sorted list
    while no_incoming:
        # current node for studying
        u = heappop(no_incoming)[1]
        # add vertice to sorted list
        sorted_list.append(u)
        # goes through current node's adjacencies except first el (insertion index)
        for v in graph[u][1:]:
            in_degree[v] -= 1
            # if node has no incoming edges push to pqqueue
            if in_degree[v] == 0:
                heappush(no_incoming,(graph[v][0],v))

    return sorted_list

def nextLine():
    line = ''
    while line == '':
        line = input().strip()
    return line

def main():
    counter = 0

    while True:
        counter +=1
        graph = {}
        n_entry = nextLine()
        n = int(n_entry)

        for i in range(n):
            beverage = input()
            graph[beverage] = [i]

        m_entry = nextLine()
        m = int(m_entry)

        for _ in range(m):
            e = nextLine()
            entry = e.split(' ')
            graph[entry[0]].append(entry[1])

        result = kahn_sort(graph)
        print("Case #"+ str(counter) + ": Dilbert should drink beverages in this order: " + ' '.join(result) + '.\n')

try:
    main()
except EOFError:
    pass
