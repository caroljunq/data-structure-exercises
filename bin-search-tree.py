# https://hackernoon.com/bst-sequences-in-python-c072c0e9b19f
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

class BinSearchTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insert(self, val):
            if(self.root == None):
                self.root = Node(val)

            else:
                self._insert(val, self.root)

    def _insert(self, val, node):
            if(val < node.data):
                if(node.left != None):
                    self._insert(val, node.left)
                else:
                    node.left = Node(val)
            else:
                if(node.right != None):
                    self._insert(val, node.right)

                else:
                    node.right = Node(val)

    def BFS(self):
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            print(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def search(root,key):

    if root is None or root.data == key:
        return root

    if root.data < key:
        return search(root.right,key)

    return search(root.left,key)

def inorder(node):
    if node.left:
        inorder(node.left)

    print(node.data)

    if node.right:
        inorder(node.right)

def preorder(node):
    print(node.data)

    if node.left:
        preorder(node.left)

    if node.right:
        preorder(node.right)

def postorder(node):
    if node.left:
        postorder(node.left)

    if node.right:
        postorder(node.right)
    print(node.data)

def height(root):

    # base condition when binary tree is empty
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1



tree = BinSearchTree()

tree.insert(31)
tree.insert(16)
tree.insert(45)
tree.insert(24)
tree.insert(7)
tree.insert(19)
tree.insert(29)

print("BFS")
tree.BFS()
print("inorder")
inorder(tree.root)
print("preorder")
preorder(tree.root)
print("postorder")
postorder(tree.root)
print(search(tree.root,9))
