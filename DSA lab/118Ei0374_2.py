class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None



def inorder(root):

    if root is not None:
        inorder(root.left)
        print(root.key)

        inorder(root.right)
def count(root):
    c = 1;
    if root is None:
        return (0)
    else:

        c += count(root.left)
        c += count(root.right)

    return(c)

def insertBST(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insertBST(node.left,key)
    else:
        node.right = insertBST(node.right,key)
    return(node)

def MinvalueBST(node):
    current = node
    while(current.left is not None):
        current = current.left
        return(current)

def MaxvalueBST(node):
    current = node
    while(current.right is not None):
        current = current.right
    return(current)
def Delete(root,key):
    if root is None:
        return (root)
    if key < root.key:
        root.left = Delete(root.left,key)
    elif(key > root.key):
        root.right = Delete(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return (temp)
        elif root.right is None:
            temp = root.left
            root = None
            return(temp)

        temp = MinvalueBST(root.right)
        root.key = temp.key
        root.right = Delete(root.right,temp.key)
    return (root)
root = None
while(1):

    print("The cases are as fallow\n1: insert\n2: Min value\n3: Max value\n4: Delete\n5: No. of Elements\n0: Exit")
    s = int(input("enter the case number"))

    if (s == 1):
        v = int(input("Enter the value you want to enter"))
        root = insertBST(root,v)


    elif (s==2):
        m = MinvalueBST(root).key
        print("Min value is ",m)+
    elif(s==3):
        M = MaxvalueBST(root).key
        print("Max value is ",M)
    elif(s==4):
        d = int(input("enter the value you want to delete"))
        Delete(root,d)
        inorder(root)
        M = MaxvalueBST(root).key
        print("Max value is ", M)
        m = MinvalueBST(root).key
        print("Min value is ", m)
    elif(s==5):
        g = count(root)
        print(g)

    elif(s==0):
        exit(0)
    else:
        print("error enter correct value")




