n_teste = input()
n = int(n_teste)
print()
# shortest path between two vertex
def bfs(g,start,end):
    queue = [[start]]
    visited = []

    if start == end:
        return queue[0]

    while queue:
        test_path = queue.pop(0)
        cur_vertex = test_path[-1]
        if cur_vertex not in visited:
            neighs = g[cur_vertex]
            for neigh2 in neighs:
                path = list(test_path)
                path.append(neigh2)
                queue.append(path)
                if neigh2 == end:
                    return path
            visited.append(cur_vertex)

while n > 0:
    results = []
    n -= 1
    num_words = 0
    words_list = []
    graph = {}
    pairs = []
    pair = 'aa'
    while num_words <= 200:
        word = input()
        if word == '*':
            break
        words_list.append(word)
        num_words += 1
    for el in words_list:
        neigh = []
        for word in words_list:
            if el != word:
                if len(el) == len(word):
                    diff_chars = sum(c1!=c2 for c1,c2 in zip(el, word))
                    if diff_chars == 1:
                        neigh.append(word)
            graph[el] = neigh
    while True and pair != '':
        try:
            pair = input()
        except EOFError:
            pair = ''
        pairs.append(pair.split(' '))
    del pairs[-1]
    for pair2 in pairs:
        result = bfs(graph,pair2[0],pair2[1])
        results.append(result)
    for result in results:
        print(result[0]+" "+result[-1]+" "+ str(len(result) - 1))
