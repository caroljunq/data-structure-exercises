class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# minimu depth of a bin search tree
def height(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    if root.left is None:
        return height(root.right)+1

    if root.right is None:
        return height(root.left) +1

    return min(height(root.left), height(root.right))+1

# # max depth bin search tree
# def height(root):
#     if root is None:
#         return 0
#
#     if root.left is None and root.right is None:
#         return 0
#
#     if root.left is None:
#         return height(root.right)+1
#
#     if root.right is None:
#         return height(root.left) +1
#
#     return max(height(root.left), height(root.right)) + 1

# Use the insert method to add nodes
n_nodes = int(input())
case_line = input()
nodes = [int(node) for node in case_line.split(' ')]

# creating tree
root = 0;

for i in range(n_nodes):
    if i == 0:
        root = Node(nodes[i])
    else:
        root.insert(nodes[i])

print(height(root))
