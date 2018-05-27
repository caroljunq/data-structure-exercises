graph = {}

def floyd_warshall(graph):
    distances = graph
    keys = graph.keys()

    for k in keys:
        for i in keys:
            for j in keys:
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    return distances

def main():
    n_case = 0
    while True:
        answer = []
        graph = {}
        for i in range(1,21):
            graph[i] = {}
            for j in range(1,21):
                if i == j:
                    graph[i][j] = 0
                else:
                    graph[i][j] = 10000
        for i in range(1,20):
            vert_line = input().strip()
            if vert_line == '':
                break
            vertices = []
            vertices = [int(x) for x in vert_line.split(' ')]
            for el in vertices[1:]:
                graph[i][el] = 1
                graph[el][i] = 1
        queries  = input()
        if queries == '':
            break
        n_queries = int(queries)
        result = floyd_warshall(graph)
        for i in range(n_queries):
            query = input().strip().split(' ')
            src = int(query[0])
            dest = int(query[1])
            answer.append((src,dest,result[src][dest]))
        n_case += 1
        print('Test Set #'+ str(n_case))
        for x,y,d in answer:
            print("%2d to %2d: %d"%(x,y,d))
        print()

try:
    main()
except EOFError:
    pass
