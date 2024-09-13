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

def postordertraversal(root):
    if root.left is not None:
        postordertraversal(root.left)

    if root.right is not None:
        postordertraversal(root.right)
    print(root.key)

def insert(root,put):
    if root is None:
        return Node(put)
    if put< root.key:
        root.left=insert(root.left,put)
    else:
        root.right=insert(root.right,put)
    return root

def search(root,sea):
    if root.key==sea:
        return True
    elif root.key<sea and root.right is not None:
        return search(root.right,sea)
    elif root.key>sea and root.left is not None:
        return search(root.left,sea)
    
    else:
        return False

        
    



def menu():
    m=int(input("1=inordertraversal\n2=preordertraversal\n3=postordertraversal"))
    if m==1:
        print(inordertraversal(tree))
    
    if m==2:
        print(preordertraversal(tree))

    if m==3:
        print(postordertraversal(tree))

        
tree=None
for i in range(12):
    ini=int(input("insert a new value"))
    tree=insert(tree,ini)
#menu()
print(search(tree,11))
