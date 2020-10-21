class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
    def insertleft(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def insertright(self,new_data):
        new_node = Node(new_data)
        if (self.head is None):
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
    def deleteright(self):
        last = self.head
        prev = self.head
        if (last is not None):
            while(last.next):
                prev = last
                last = last.next
            prev.next = None
            print("\n" , last.data,"is deleted\n")
    def deleteleft(self):
        tmp = self.head
        if (tmp is not None):

            next = tmp.next
            print("\n" , tmp.data,"is deleted\n")
            tmp = None
            self.head = next
    def print(self):
        if(self.head is None):
            print("queue is empty")
            return
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next

q = Queue()

q.head = Node(1)
second = Node(2)
third = Node(3)
q.head.next = second
second.next = third
while(1):
    print("1: restricted input queue\n2: restricted output queue\n3: printing\n0: exit")
    s = int(input())
    if(s == 1):
        while(1):

            print("restricted input will be done form left")
            print("11: insert left\n12: delete left\n13: delete right\n14: printing\n15: exit")
            a = int(input())
            if(a == 11):
                print("enter the number you want to enter")
                i = int(input())
                q.insertleft(i)
                q.print()
            elif(a == 12):
                q.deleteleft()
                q.print()
            elif(a == 13):
                q.deleteright()
                q.print()
            elif(a == 14):
                q.print()
            elif(a == 15):
                break
            else:
                print("error enter correct number")
    elif(s == 2):
        while(1):

            print("restricted output will be done form right")
            print("21: insert left\n22: insert right\n23: delete right\n24: printing\n25: exit")
            a = int(input())
            if(a == 21):
                print("enter the number you want to enter")
                i = int(input())
                q.insertleft(i)
                q.print()
            elif(a == 22):
                print("enter the number you want to enter")
                i = int(input())
                q.insertright(i)
                q.print()
            elif(a == 23):
                q.deleteright()
                q.print()
            elif(a == 24):
                q.print()
            elif(a == 25):
                break
            else:
                print("error enter correct number")
    elif(s == 3):
        q.print()
    elif(s == 0):
        exit(0)
    else:
        print("error enter correct number")



