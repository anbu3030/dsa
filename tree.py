class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def inordertraversal(root):
    if root.left is not None:
        inordertraversal(root.left)
    print(root.key)

    if root.right is not None:
        inordertraversal(root.right)

def preordertraversal(root):
    print(root.key)
    if root.left is not None:
        preordertraversal(root.left)

    if root.right is not None:
        preordertraversal(root.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
inordertraversal(root)
preordertraversal(root)