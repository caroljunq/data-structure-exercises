# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
q = int(input())
n_queries = 0


def bfs(graph, root, n_nodes):
    #keep a list of visited nodes
    visited = [root]
    distances = {k: 0 for k in graph.keys()}

    queue = [root]
    #while queue has elements to visit the adjacencies
    while(len(queue) > 0):
        v = queue[0]
        # verify adjacencies for vertice v
        for cur in graph[v]:
            #if node has never been visited
            if cur not in visited:
                #mark as visited
                visited.append(cur)
                #add in queue to explore your adjacencies
                queue.append(cur)
                distances[cur] = distances[v] + 6

        #remove first element from queue, because it's already been visited
        queue.pop(0)
    #returns the elements in the order they were visited
    results = []
    for key in range(1, n_nodes + 1):
        if key != root:
            if distances[key] == 0:
                results.append(-1)
            else:
                results.append(distances[key])
    return results


outputs = []
while n_queries < q:
    case_line = input()
    n, m = [int(x) for x in case_line.split(' ')]
    graph = {node: [] for node in range(1, n + 1)}
    n_queries += 1

    # getting edges
    for _ in range(m):
        edge = input()
        u, v = edge.split(' ')
        graph[int(u)].append(int(v))
        graph[int(v)].append(int(u))

        # getting starting node
    s = int(input())
    outputs.append(bfs(graph, s, int(n)))

for i in range(len(outputs)):
    print(' '.join([str(el) for el in outputs[i]]))
