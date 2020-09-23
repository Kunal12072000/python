class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def inserAfter(self,prev_node,new_data):
        if(prev_node is None):
            print("error")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def append(self,new_data):
        new_node = Node(new_data)
        if (self.head is None):
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
    def deleteNode(self,key):
        tmp = self.head
        if(tmp is not None):
            if(tmp.data == key):
                self.head = tmp.next
                tmp = None
                return
            while(tmp is not None):
                if tmp.data == key:
                    break
                prev = tmp
                tmp = tmp.next
            if(tmp == None):
                return
            prev.next = tmp.next
            tmp = None
    def deletePosition(self,position):
        if self.head == None:
            return
        tmp = self.head
        if position ==0:
            self.head = tmp.next
            tmp = None
            return
        for i in range (position - 1):
            tmp = tmp.next
            if tmp is None:
                break
        if tmp is None:
            return
        if tmp.next is None:
            return
        tmp.next = tmp.next.next
    def count(self):
        tmp = self.head
        count = 0
        while(tmp):
            count += 1
            tmp = tmp.next
        return count
    def swap(self,x,y):
        if x == y:
            return
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
        if currY == None and currX == None:
            return
        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY
        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX
        tmp = currX.next
        currX.next = currY.next
        currY.nect = tmp
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
    def mergelist(self,head1,head2):
        tmp = None
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        if head1.data<=head2.data:
            tmp = head1
            tmp.next = mergelist(head1.next,head2)
        else:
            tmp = head2
            tmp.next = mergelist(head1,head2.next)
        return tmp
    def middle(self,head):
        if (head == None):
            return head
        slow = head
        fast = head
        if(fast.next != None and fast.next.next != None):   # because in even case if we dont do next.next = None the it would coulse problem
            slow = slow.next
            fast = fast.next.next
        return slow
    def sort(self,head):
        if h == None or h.next == None:
            return head
        middle = self.middle(head)
        nexttomiddle = middle.next

        middle.next = None

        left = self.sort(head)
        right = self.sort(nexttomiddle)
        sortedlist = self.mergelist(left,right)
        return sortedlist
    def partReverse(self,head,k):
        if head == None:
            return head
        current = head
        prev = None
        next = None
        count = 0
        while(current is not None and count<k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count +=1
        if next is not None:
            head.next = self.partReverse(next,k)
        return prev
    def removeloop(self,loop_node):
        p1 = loop_node
        p2 = loop_node
        k = 1
        while (p1.next != p2):
            p1 = p1.next
            k += 1
        p1 = self.head
        p2 = self.head
        for i in range(k):
            p2 = p2.next
        while(p1.next != p2.next):
            p1 = p1.next
            p2 = p2.next
        p2.next = None
    def find_loop(self):
        fast = self.head
        slow = self.head
        while(slow,fast,fast.next):
            slow = slow.next
            fast = fast.next.next
            if (fast == slow):
                self.removeloop(slow)
                return 1
        return  0
    def sum(self, head1,head2):
        carry = 0
        prev = None
        tmp = None
        while(head1 is not None or head2 is not None):
            data1 = 0 if head1 is None else head1.data
            data2 = 0 if head2 is None else head2.data
            sum = carry + data1 +data2
            carry = 1 if sum >= 10 else 0
            sum = sum if sum < 10  else sum%10
            tmp = Node(sum)
            if sum.head is None:
                self.head = tmp
            else:
                prev.next = tmp
            prev = tmp
            if head1 is not None:
                head1 = head1.next
            if head2 is not None:
                head2 = head2.next
        if carry > 0:
            tmp.next = Node(carry)

    def rotate(self,k):
        if k == 0:
            return
        current = self.head
        count = 1
        while(count , k and current is not None):
            current = current.next
            count+=1

        if current is None:
            return
        kthNode = current
        while(current.next is not None):
            current = current.next
        current.next = self.head
        self.head = kthNode.next
        kthNode.next = None








if __name__=='__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.append(6)
    llist.push(9)
    llist.inserAfter(second,15)
    llist.deleteNode(3)


    llist.printList()
    print(llist.count(),"i am groot")