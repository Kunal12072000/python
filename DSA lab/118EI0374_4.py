class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class doublyLinked:
    def __init__(self):
        self.head = None
    def insertbig(self,data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    def insertend(self,data):
        new_node = Node(data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while(last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last
        return
    def insertafter_givennode(self,prev_node,data):
        new_node = Node(data)
        if self.head is None:
            print("the list is empty")
            new_node.prev = None
            self.head = new_node
            return
        if prev_node is None:
            print("the given node does'nt exit")
            return

        new_node.prev = prev_node
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node


    def insertafter(self,prev_value,data):
        new_node = Node(data)
        if self.head is None:
            print("the list is empty")
            new_node.prev = None
            self.head = new_node
            return
        prev_node = self.head
        while(prev_node.data != prev_value):
            prev_node = prev_node.next
        if prev_node == None:
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
            new_node.prev = None
            self.head = new_node
            return
        prev_node = self.head
        while (prev_node.data != prev_value):
            prev_node = prev_node.next
        if prev_node == None:
            print("the given does not exit")
            return
        new_node.next = prev_node
        new_node.prev = prev_node.prev
        prev_node.prev = new_node
        if new_node.prev is not None:
            new_node.prev.next = new_node


    def insertbefore_givennode(self,prev_node,data):
        new_node = Node(data)
        if self.head is None:
            print("the list is empty")
            new_node.prev = None
            self.head = new_node
            return
        if prev_node is None:
            print("the given node does'nt exit")
            return

        new_node.next = prev_node
        new_node.prev = prev_node.prev
        prev_node.prev = new_node
        if new_node.prev is not None:
            new_node.prev.next = new_node
    def reverse_list(self):
        if (self.head == None or self.head.next == None):
            return None
        curr = self.head
        tmp = None
        while(curr is not None):
            tmp = curr.prev
            curr.prev = curr.next
            curr.next = tmp
            curr = curr.prev
        if(tmp is not None):

            self.head = tmp.prev
    def print(self):
        if self.head is None:
            print("The list is empty")
            return
        curr = self.head
        while(curr is not None):
            print(curr.data)
            curr = curr.next
    def print_elementsafter(self,node):
        if self.head is None:

            print("the given list is empty")
            return
        print("\n transversal in forward direction")
        while(node is not None):
            print(node.data)
            node = node.next
    def print_elementsbefore(self,node):
        if self.head is None:

            print("the given list is empty")
            return
        print("\n transversal in backword direction")
        while(node is not None):
            print(node.data)
            node = node.prev

    def delete_first(self):
        if self.head is None:
            print("the list is empty")
            return
        curr = self.head.next
        self.head = curr
        curr.prev = None
    def delete_last(self):
        if(self.head is None):
            print("the given list is empty")
            return
        curr = self.head
        while(curr.next is not None):
            curr = curr.next
        curr.prev.next = None
    def delete_after_node(self,node):
        if (self.head is None):
            print("the given list is empty")
            return
        if node is None:
            print("the node does'nt exist")
            return
        curr = node.next.next
        node.next.next.prev = node
        node.next = curr
    def delete_before_node(self,node):
        if (self.head is None):
            print("the given list is empty")
            return
        if node is None:
            print("the node does'nt exist")
            return
        curr = node.prev.prev
        node.prev.prev.next = node
        node.prev = curr
    def delete_before_value(self,node_value):
        if (self.head is None):
            print("the given list is empty")
            return
        node = self.head
        while(node.data != node_value):
            node = node.next
        if node is None:
            print("the node does'nt exist")
            return
        curr = node.prev.prev
        node.prev.prev.next = node
        node.prev = curr
    def delete_after_value(self,node_value):
        if (self.head is None):
            print("the given list is empty")
            return
        node = self.head
        while (node.data != node_value):
            node = node.next
        if node is None:
            print("the node does'nt exist")
            return
        curr = node.next.next
        node.next.next.prev = node
        node.next = curr


DLL = doublyLinked()
while(1):
    print("1: Insert \n2: delete\n3: reverse\n4:print\n0: exit")
    s_m = int(input())
    if (s_m == 1):
        while(1):

            print("11: insert at big\n12: insert at end\n13: insert after n node\n14:insert after given value\n15:insert before n node\n16: insert before vaule\n10:exit")
            s_1 = int(input())
            if(s_1 == 11):
                data = int(input("enter value"))
                DLL.insertbig(data)
                DLL.print()
            elif(s_1 == 12):
                data = int(input("enter value"))
                DLL.insertend(data)
                DLL.print()
            elif(s_1 == 13):
                data = int(input("enter value"))
                n = int(input("enter  number of node"))
                node = DLL.head
                for i in range(n):
                    node = node.next
                DLL.insertafter_givennode(node,data)
                DLL.print()
            elif(s_1 == 14):
                data = int(input("enter the value to be entered"))
                node_value = int(input("enter the value after which need to insert"))
                DLL.insertafter(node_value,data)
                DLL.print()
            elif(s_1 == 15):
                data = int(input("enter value"))
                n = int(input("enter  number of node"))
                node = DLL.head
                for i in range(n):
                    node = node.next
                DLL.insertbefore_givennode(node,data)
                DLL.print()
            elif(s_1 == 16):
                data = int(input("enter the value to be entered"))
                node_value = int(input("enter the value after which need to insert"))
                DLL.insertbefore(node_value ,data)
                DLL.print()
            elif(s_1 == 10):
                break
    if (s_m == 2):
        while(1):

            print("21: delete at big\n22: delete at end\n23: delete after n node\n24:delete after given value\n25:delete before n node\n26: delete before vaule\n20:exit")
            s_2 = int(input())
            if (s_2 == 21):
                DLL.delete_first()
                DLL.print()
            elif (s_2 == 22):
                DLL.delete_last()
                DLL.print()
            elif (s_2 == 23):
                n = int(input("enter  number of node"))
                node = DLL.head
                for i in range(n):
                    node = node.next
                DLL.delete_after_node(node)
                DLL.print()
            elif (s_2 == 24):

                node_value = int(input("enter the value after which need to insert"))
                DLL.delete_after_value(node_value)
                DLL.print()
            elif (s_2 == 25):

                n = int(input("enter  number of node"))
                node = DLL.head
                for i in range(n):
                    node = node.next
                DLL.delete_before_node(node)
                DLL.print()
            elif (s_2 == 26):

                node_value = int(input("enter the value after which need to insert"))
                DLL.delete_before_value(node_value)
                DLL.print()
            elif (s_2 == 20):
                break
    elif (s_m == 3):
        DLL.reverse_list()
        DLL.print()
    elif(s_m == 4):
        while(1):

            print("41: normal printting\n42: print after n node\n43: print before annode\n44: exit")
            s_3 = int(input())
            if(s_3 == 41):
                DLL.print()
            elif(s_3 == 42):
                n = int(input("enter  number of node"))
                node = DLL.head
                for i in range(n):
                    node = node.next
                DLL.print_elementsafter(node)
            elif(s_3 == 43):
                n = int(input("enter  number of node"))
                node = DLL.head
                for i in range(n):
                    node = node.next
                DLL.print_elementsbefore(node)
            elif(s_3 == 44):
                break
    elif(s_m == 0):
        exit(0)
    else:
        print("error enter correct value")