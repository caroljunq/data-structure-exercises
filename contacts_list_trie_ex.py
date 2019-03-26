# https://www.hackerrank.com/challenges/contacts/leaderboard?page=5
trieDict = {}
def add_word(word):
    currentLevel = trieDict
    for char in word:
        if char not in currentLevel:
            currentLevel[char] = {}
            currentLevel[char]['count'] = 1
        else:
            currentLevel[char]['count'] += 1
        currentLevel = currentLevel[char]
    currentLevel[None] = None

def find_prefix(word):
    currentLevel = trieDict
    for char in word:
        if char not in currentLevel:
            return 0
        currentLevel = currentLevel[char]
    return currentLevel['count']

n_queries = int(input())

for _ in range(n_queries):
    comd, word = input().split()
    if comd == 'add':
        add_word(word)
    else:
        print(find_prefix(word))
