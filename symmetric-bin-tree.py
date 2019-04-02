class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def BFS(root):
    queue = [root]
    res = []
    while queue:
        node = queue.pop(0)
        res.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res


def inorder(root):
    if root == None:
        return []

    left_list = inorder(root.left)
    right_list = inorder(root.right)

    return left_list + [root.data] + right_list


# duas subarvores iguais
def isSymmetricEqual(root):
    res_left = []
    res_right = []

    res_left = BFS(root.left)
    res_right = BFS(root.right)

    print(res_left)
    print(res_right)
    return res_left == res_right

def isSymmetricMirror(root):
    left_order = inorder(root.left)
    right_order = inorder(root.right)

    return left_order == right_order[::-1]

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

print(isSymmetricMirror(root))
