def iterative_reverse(word):
    stack = []

    for c in word:
        stack.append(c)

    while stack:
        c = stack.pop()
        print(c)

def recursive_reverse_string(word):
    if not word:
        return word
    return recursive_reverse_string(word[1:]) + word[0]

def countChar(word):

    if not word:
        return 0

    return countChar(word[1:]) + 1


# iterative_reverse("mariana")
print(recursive_reverse_string("mariana"))
print(countChar("carol"))
