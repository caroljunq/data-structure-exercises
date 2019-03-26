
# https://www.hackerrank.com/challenges/swap-nodes-algo/problem
depths = {}
tree = {}

def populate_depths(node, depth):
    if depth not in depths.keys() and node > 0:
        depths[depth] = []
    if node == -1:
        return
    depths[depth].append(node)
    for child in tree[node]:
        populate_depths(child, depth + 1)

def in_order_print(T,start):
    if start == -1:
        return
    in_order_print(T,T[start][0])
    print(start, end=' ')
    in_order_print(T,T[start][1])
    if start == 1:
        print('')

def swap(T, k):
    for depth in range(2,max(depths.keys()) + 1):
        if (depth - 1) % k == 0:
            for node in depths[depth-1]:
                T[node] = [tree[node][1],tree[node][0]]
    in_order_print(T,1)

n = int(input())
tree = {i: [-1,-1] for i in range(1, n+1)}

for i in range(1,n+1):
    a,b = [int(el) for el in input().split()]
    tree[i] = [a,b]


populate_depths(1,1)

t = int(input())

for _ in range(t):
    k = int(input())
    swap(tree, k)
