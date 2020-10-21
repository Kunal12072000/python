class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class circulardoublyLinked:
    def __init__(self):
        self.head = None
    def insertbig(self,data):
        new_node = Node(data)
        new_node.next = self.head



        if self.head is not None:
            self.head.prev = new_node
            last = self.head
            while (last.next is not self.head):
                last = last.next

            last.next = new_node
            new_node.prev = last
            self.head = new_node
        else:
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
        return
    def insertend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is None:
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
            return
        last = self.head
        while(last.next is not self.head):
            last = last.next
        last.next = new_node
        new_node.prev = last
        self.head.prev = new_node
        return



    def insertafter(self,prev_value,data):
        new_node = Node(data)
        if self.head is None:
            print("the list is empty")
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
            return
        prev_node = self.head
        while(prev_node.data != prev_value and prev_node.next != self.head):
            prev_node = prev_node.next
        if prev_node.next == self.head:
            print("the given does not exit")
            return
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node
    def insertbefore(self,prev_value,data):
        new_node = Node(data)
        if self.head is None:
            print("the list is empty")
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
            return
        prev_node = self.head
        while (prev_node.data != prev_value and prev_node.next != self.head):
            prev_node = prev_node.next
        if prev_node.next == self.head:
            print("the given does not exit")
            return
        new_node.next = prev_node
        new_node.prev = prev_node.prev
        prev_node.prev = new_node
        if new_node.prev is not None:
            new_node.prev.next = new_node




    def print(self):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.next == self.head:
            print(self.head.data)
            return
        curr = self.head
        while(curr is not curr.next != self.head):
            print(curr.data)
            curr = curr.next
        print(curr.data)
    def delete_first(self):
        if self.head is None:
            print("the list is empty")
            return
        if (self.head.next == self.head):
            self.head = None
            print("list is empty")
            return

        last = self.head
        while (last.next is not self.head):
            last = last.next

        curr = self.head.next
        self.head = curr
        curr.prev = last
        last.next = curr
    def delete_last(self):
        if(self.head is None):
            print("the given list is empty")
            return
        if(self.head.next == self.head):
            self.head = None
            print("list is empty")
            return
        curr = self.head
        while(curr.next is not self.head):
            curr = curr.next
        curr.prev.next = self.head
        self.head.prev = curr.prev
    def delete_node(self,node_value):
        if self.head is None:
            print("the list is empty")
            return
        if (self.head.next == self.head):
            self.head = None
            print("list is empty")
            return
        curr = self.head
        while(curr.data != node_value and curr.next != self.head):
            curr = curr.next
        if curr.next == self.head:
            print("error the node not found")
            return
        curr.next.prev = curr.prev
        curr.prev.next = curr.next
        print(node_value,"is deleted")




CDLL = circulardoublyLinked()
while(1):
    print("1: Insert \n2: delete\n3: print\n0: exit")
    s_m = int(input())
    if (s_m == 1):
        while(1):

            print("11: insert at big\n12: insert at end\n13:insert after given value\n14: insert before vaule\n10:exit")
            s_1 = int(input())
            if(s_1 == 11):
                data = int(input("enter value"))
                CDLL.insertbig(data)
                CDLL.print()
            elif(s_1 == 12):
                data = int(input("enter value"))
                CDLL.insertend(data)
                CDLL.print()

            elif(s_1 == 13):
                print("##note the node after which to be inserted must not be ending##")
                data = int(input("enter the value to be entered"))
                node_value = int(input("enter the value after which need to insert"))
                CDLL.insertafter(node_value,data)
                CDLL.print()

            elif(s_1 == 14):
                print("##note the node before which to be inserted must not be bigining##")
                data = int(input("enter the value to be entered"))
                node_value = int(input("enter the value after which need to insert"))
                CDLL.insertbefore(node_value ,data)
                CDLL.print()
            elif(s_1 == 10):
                break
    if (s_m == 2):
        while(1):

            print("21: delete at big\n22: delete at end\n23: delete node\n20:exit")
            s_2 = int(input())
            if (s_2 == 21):
                CDLL.delete_first()
                CDLL.print()
            elif (s_2 == 22):
                CDLL.delete_last()
                CDLL.print()
            elif (s_2 == 23):
                n = int(input("enter the node want to delete"))
                CDLL.delete_node(n)
                CDLL.print()

            elif (s_2 == 20):
                break

    elif(s_m == 3):
        CDLL.print()
    elif(s_m == 0):
        exit(0)
    else:
        print("error enter correct value")