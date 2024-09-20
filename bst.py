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
    
def inordersuccessor(root):
    succes=root.right
    while succes.left is not None:
        succes=succes.left
    return succes 

def delete(root,tup):
    if root is None: 
        return root
    if tup < root.key:
        root.left=delete(root.left,tup)

    elif tup > root.key:
        root.right=delete(root.right,tup)

    else:
        if root.right is None:
          return root.left
        
        if root.left is None:
          return root.right
        
        c=inordersuccessor(root)
        root.key=c.key
        root.right=delete(root.right,c.key)

    return root
def menu():
    m=int(input("1=inordertraversal\n2=preordertraversal\n3=postordertraversal\n4=search"))
    if m==1:
        print(inordertraversal(tree))
    
    if m==2:
        print(preordertraversal(tree))

    if m==3:
        print(postordertraversal(tree))
    
    if m==4:
        z=int(input("what number are you searching for"))
        print(search(tree,z))

        
tree=None
for i in range(6):
    ini=int(input("insert a new value"))
    tree=insert(tree,ini)
menu()
