# UVA 429 - Word Transformation

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

n = int(input())
results = []
while n > 0:
    dicio = {}
    words_list = []
    num_words = 0
    pairs = []
    while num_words < 201:
        word = input()
        if word == '*':
            break
        words_list.append(word)
        num_words += 1
    # check word
    for el in words_list:
        neigh = []
        for word in words_list:
            if el != word:
                if len(el) == len(word):
                    diff = sum(c1!=c2 for c1,c2 in zip(el, word))
                    if diff == 1:
                        neigh.append(word)
        dicio[el] = neigh
    comparing = 'aa'
    while comparing != '':
        try:
            comparing = input()
        except EOFError:
            comparing = ''
        if comparing == '':
            break
        pairs.append(comparing.split(' '))
    group = []
    for w1,w2 in pairs:
        answer = bfs_path_between(dicio,w1,w2)
        group.append(w1 + ' ' + w2 + ' '+ str(len(answer) - 1))
    results.append(group)
    n -= 1

for i in range(len(results)):
    for j in results[i]:
        print(j)
    if i != len(results) - 1:
        print()
