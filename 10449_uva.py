# 10449 Uva Challenge

from sys import maxsize as inf

answers = []

def bell_ford(graph, source):
    distances = {}

    for v in graph:
        if v == source:
            distances[v] = 0
        else:
            distances[v] = inf

    for _ in range(0, len(graph) - 1):
        for u in graph:
            for edge in graph[u]:
                v = edge[0]
                w = edge[1]
                if distances[u] != inf:
                    if (distances[u] + w) < distances[v]:
                        distances[v] = distances[u] + w

    #checking for negative, if is true, set the new distance as INFINITY
    for u in graph:
        for v, w in graph[u]:
            if distances[u] + w < distances[v]:

    return distances

while(True):
    try:
        busyness_str = input()
    except EOFError:
        pass
    if busyness_str == '':
        break
    busyness = list(map(int, busyness_str.split(' ')))
    graph = {}
    n_questions = 0;
    questions = []
    answer = []
    result = []

    if len(busyness) == busyness[0] + 1 and busyness[0] < 21: #verificar se busyness.length == b[0] + 1
        n_junct = int(input())
    else:
        sys.exit()

    for i in range(busyness[0]):
        graph[i+1] = []

    while n_junct > 0 and n_junct < 201:
        pair = input()
        el1 = int(pair[0])
        el2 = int(pair[2])
        graph[el1].append((el2, (busyness[el2] - busyness[el1]) ** 3))
        n_junct -= 1

    n_question = int(input())

    while n_question > 0:
        questions.append(int(input()))
        n_question -= 1

    result = bell_ford(graph, 1)
    for i in questions:
        if result[i] < 3 or result[i] == inf: #or se tiver num caminho cuja soma passou por um edge negativo
            answer.append('?')
        else:
            answer.append(result[i])
    answers.append(answer)

for i in range(len(answers)):
    print("\r\rSet #" + str(i+1))
    for el in answers[i]:
        print(el)
