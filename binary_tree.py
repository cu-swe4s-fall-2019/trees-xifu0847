class Node:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


def insert(root, key, value=None):
    if root is None:
        return Node(key, value)
    if root.key > key:
        root.left = insert(root.left, key, value)
    else:
        root.right = insert(root.right, key, value)
    return root


def search(root, key):
    if root is None or root.key == key:
        return root
    if root.key > key:
        return search(root.left, key)
    return search(root.right, key)


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)
