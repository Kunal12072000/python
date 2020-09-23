class stacknodes:
    def __init__(self,data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.root = None
    def isempty(self):
        return True if self.root == None else False
    def push(self,data):
        newNode = stacknodes(data)
        newNode.next = self.root
        self.root = newNode
    def pop(self):
        if self.isempty():
            return float("-inf")
        tmp = self.root
        self.root = self.root.next
        popped = tmp.data
        return popped
    def peek(self):
        if self.isempty():
            return float("-inf")
        popped = self.root.data
        return popped
stack = stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())


