# BFS Algorithm --> Breadth First Search
def bfs(graph, root):
    #keep a list of visited nodes
    visited = [root]
    #queue to save the adjacencies
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
        #remove first element from queue, because it's already been visited
        queue.pop(0)
    #returns the elements in the order they were visited
    return visited

# BFS Shortest path
# shortest path between two vertex
def bfs_path_between(graph, begin, end):
    #queue of paths (queues)
    #starts with begin (first node from path)
    queue = [[begin]]
    # test if path is from 'begin' to 'begin'
    if begin == end:
        return queue[0]
    # stores seen nodes
    seen = []
    while queue:
        # the path to be tested
        path_to_test = queue.pop(0)
        # get the last node from the "path_to_test"
        last_node = path_to_test[-1]
        # goes through the neighborhood of the last_node in graph if its
        if last_node not in seen:
            for neigh in graph[last_node]:
                partial_path = list(path_to_test)
                partial_path.append(neigh)
                queue.append(partial_path)
                # verify if the current neighboor is equal to "end"
                if neigh == end:
                    return partial_path
            seen.append(last_node)

# DFS - Deepth First Search
def dfs(graph, start, visited):
    visited.append(start)
    for v in graph[start]:
        if v not in visited:
            dfs(graph,v,visited)
    return visited


graph = {
  'A': ['B','D','G'],
  'B': ['A','E','F'],
  'C': ['F','H'],
  'D': ['A','F'],
  'E': ['B','G'],
  'F': ['C','D'],
  'G': ['A','E'],
  'H': []
}

# For testing bfs path between

print(bfs_path_between(graph,'A','F'))
