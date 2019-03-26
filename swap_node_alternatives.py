from __future__ import print_function
from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

dton = defaultdict(list)


def populate_dton(node, depth):
    if node == -1:
        return
    dton[depth].append(node)
    for child in tree[node]:
        populate_dton(child, depth + 1)

def swap(node):
    tree[node] = tree[node][::-1]

def print_below(node):
    if node == -1:
        return
    print_below(tree[node][0])
    print(node, end=' ')
    print_below(tree[node][1])
    if node == 1:
        print('')

tree = {}
N = int(raw_input())
for n in range(1, N + 1):
    tree[n] = map(int, raw_input().rstrip().split(' '))

populate_dton(1, 1)
depth_max = max(dton.keys())
T = int(raw_input())
Ks = [int(raw_input()) for _ in range(T)]
for Ki in Ks:
    for di in range(Ki, depth_max + 1, Ki):
        swap_nodes = dton[di]
        for nodei in swap_nodes:
            swap(nodei)
    print_below(1)
            
