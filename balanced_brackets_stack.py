
# https://www.hackerrank.com/challenges/balanced-brackets/problem
# Trie Exercise
opening = ['[','{','(']

closing = [']','}',')']
def isBalanced(s):
    stack = []
    # odd
    size  = len(s)
    count = 0
    # even num of characters
    for c in s:
        if c in opening:
            stack.append(c)
        else:
            if len(stack) > 0:
                cur = stack.pop()
                if opening.index(cur) == closing.index(c):
                    count += 1
            else:
                return 'NO'

    if len(stack) == 0 and count == int(size / 2):
        return 'YES'
    else:
        return 'NO'

n = int(input())
n_cases = 0

while n_cases < n:
    s = input()
    print(isBalanced(s))
    n_cases += 1


# alternative
    # opening = tuple('({[')
    # closing = tuple(')}]')
    # mapping = dict(zip(opening, closing))
    # queue = []
    #
    # for letter in expression:
    #     if letter in opening:
    #         queue.append(mapping[letter])
    #     elif letter in closing:
    #         if not queue or letter != queue.pop():
    #             return False
    # return not queue
