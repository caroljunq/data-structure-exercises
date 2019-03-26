# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
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


# def height(root):
#     if root is None:
#         return 0
#
#     if root.left is None and root.right is None:
#         return 0
#
#     if root.left is None:
#         return height(root.right) + 1
#
#     if root.right is None:
#         return height(root.left) + 1
#
#     return max(height(root.left), height(root.right)) + 1

def height(root):
    if root is None:
        return 0 ;

    else :

        # Compute the depth of each subtree
        lDepth = height(root.left)
        rDepth = height(root.right)

        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
