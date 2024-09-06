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

def insert(root,put):
    if root is None:
        return Node(put)
    if put< root.key:
        root.left=insert(root.left,put)
    else:
        root.right=insert(root.right,put)
    return root

tree=None
for i in range(8):
    ini=int(input("insert a new value"))
    tree=insert(tree,ini)
inordertraversal(tree)