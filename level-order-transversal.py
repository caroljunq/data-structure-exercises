# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
# iterative
def breadth_first_search(root):
    to_visit = []
    if root:
        to_visit.append(root)
    while to_visit:
        current = to_visit.pop(0)
        print(current.info)
        if current.left:
            to_visit.append(current.left)
        if current.right:
            to_visit.append(current.right)

# recursive
def levelOrder(queue):
    if len(queue) == 0:
        return []

    root = queue[0]

    queue.pop(0)

    if root.left:
        queue.append(root.left)

    if root.right:
        queue.append(root.right)

    print(root.info)
    levelOrder(queue)


tree = BinarySearchTree()

arr = list(map(int, input().split()))

for i in range(len(arr)):
    tree.create(arr[i])

print(breadth_first_search(tree.root))
print(levelOrder([tree.root]))
