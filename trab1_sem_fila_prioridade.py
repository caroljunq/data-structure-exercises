# Topological Sort
def kahn_sort(graph):
    #list with sorted nodes
    sorted_list = []
    #nodes without incoming edges
    no_incoming = []

    #stores in_degree for each node
    in_degree = {}

    # count incoming edges for each node
    for u in graph:
        in_degree[u] = 0
        for v in graph:
            if u in graph[v]:
                in_degree[u] += 1

    # select all nodes with 0 incoming edges
    for v in graph:
        if in_degree[v] == 0:
            no_incoming.append(v)

    while len(no_incoming) > 0:
        u = no_incoming.pop(0)
        sorted_list.append(u)
        for v in graph[u]:
            index = graph[u].index(v)
            in_degree[v] -= 1
            if in_degree[v] == 0:
                no_incoming.append(v)

    return sorted_list if len(sorted_list) == len(in_degree) else []

graph1 = {
    'wine': ['cachaca'],
    'beer': ['cachaca','rum','wine'],
    'rum': [],
    'apple': ['beer','rum'],
    'cachaca': []
}

graph = {
    'cachaca': [],
    'rum': ['cachaca','gin'],
    'apple': ['gin','martini','beer'],
    'tequila': [],
    'whiskey': [],
    'wine': ['whiskey','vodka'],
    'vodka': ['tequila'],
    'beer': ['whiskey','rum','tequila'],
    'martini': [],
    'gin': []

}
graph2 = {
    'a': ['c','b'],
    'b': ['f'],
    'c': [],
    'd': ['c','e'],
    'e': [],
    'f': ['e']
}

graph5 = {
    0: [1],
    1: [2],
    2: [ ],
    3: [1],
    4: [2]
}

print(kahn_sort(graph3))
