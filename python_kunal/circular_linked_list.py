class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.last = None
    def addTOempty(self,data):
        if(self.last != None):
            return self.last
        tmp = Node(data)
        self.last = tmp
        self.last.next = self.last
        return self.last
    def addBegin(self,data):
        if(self.last ==None):
            return self.addTOempty(data)
        tmp = Node(data)
        tmp.next = self.last.next
        self.last.next = tmp
        return self.last
    def addend(self,data):
        if(self.last == None):
            return self.addTOempty(data)
        tmp = Node(data)
        tmp.next = self.last.next
        self.last.next = tmp
        self.last = tmp
        return self.last
    def addafter(self,data,item):
        if(self.last == None):
            return
        tmp = Node(data)
        p = self.last.next
        while p:
            if(p.data == item):
                tmp.next = p.next
                p.next = tmp
                if(p == self.last):

                    self.last = tmp
                else:
                    return self.last
            p = p.next
            if(p == self.last.next):
                print("error item not present")
                break
    def transverse(self):
        if(self.last == None):
            print("error the list is empty")
            return
        tmp = self.last.next
        while(tmp):
            print(tmp.data,end = " ")
            tmp = tmp.next
            if(tmp == self.last.next):
                break
    def sortinsert(self,new_node):
       current = self.head
        if current is None:
            new_node.next = new_node
            self.head = new_node
        elif(current.data >= new_node.data):
            while(current.next != self.head):
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            while(current.next != self.head and current.data < new_node.data):
                current = current.next
            new_node.next = current.next
            current.next = new_node


if __name__ == '__main__':
    llist = CircularLinkedList()

    last = llist.addTOempty(6)
    last = llist.addBegin(4)
    last = llist.addBegin(2)
    last = llist.addend(8)
    last = llist.addend(12)
    last = llist.addafter(10, 8)

    llist.transverse()

