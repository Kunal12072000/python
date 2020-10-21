class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


    def binaryinsert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.binaryinsert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.binaryinsert(data)
        else:
            self.data = data
    def printtree(self):
            print(self.data)
    def printTreechild(self):
        if self.right:
            print(self.right.data)
        if self.left:
            print(self.left.data)
        else:
            print("0")

root = Node("B")
root.binaryinsert("D")
root.binaryinsert("E")
root.binaryinsert("T")
root.binaryinsert("E")
root.binaryinsert("M")
root.binaryinsert("N")
root.binaryinsert("P")
root.printtree()
root.printTreechild()