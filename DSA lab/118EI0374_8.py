import sys
class MinHeap:

    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1
    def parent(self,pos):
        return(pos//2)
    def leftChild(self,pos):
        return(2*pos)
    def rightChild(self,pos):
        return ((2*pos ) + 1 )
    def isLeaf(self,pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False
    def swap(self,fpos,spos):
        self.Heap[fpos],self.Heap[spos] = self.Heap[spos],self.Heap[fpos]
    def minHeapify(self,pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or self.Heap[pos] > self.Heap[self.rightChild(pos)]):
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos,self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos,self.rightChild(pos))
                    self.minHeapify((self.rightChild(pos)))

    def insert(self,node):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = node
        current = self.size
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def print(self):
        if self.size == 0:
            print("<---EMPTY--->")
        else:
            for i in range(1,(self.size//2)+1):
                print("parent : "+str(self.Heap[i])+" left child :"+str(self.Heap[2*i])+" right child :"+str(self.Heap[2*i + 1]))

    def minHeap(self):
        for pos in range(self.size//2,0,-1):
            self.minHeapify(pos)
    def delete(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return(popped)

class MaxHeap:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1
    def parent(self,pos):
        return(pos//2)
    def leftChild(self,pos):
        return(2*pos)
    def rightChild(self,pos):
        return ((2*pos ) + 1 )
    def isLeaf(self,pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False
    def swap(self,fpos,spos):
        self.Heap[fpos],self.Heap[spos] = self.Heap[spos],self.Heap[fpos]
    def maxHeapify(self,pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or self.Heap[pos] < self.Heap[self.rightChild(pos)]):
                if self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]:
                    self.swap(pos,self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))
                else:
                    self.swap(pos,self.rightChild(pos))
                    self.maxHeapify((self.rightChild(pos)))
    def insert(self,node):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = node
        current = self.size
        while self.Heap[current] > self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
    def delete(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)
        return(popped)
    def print(self):
        if self.size == 0:
            print("<---EMPTY--->")
        else:
            for i in range(1,(self.size//2)+1):
                print("parent : "+str(self.Heap[i])+" left child :"+str(self.Heap[2*i])+" right child :"+str(self.Heap[2*i + 1]))


while(1):
    s = int(input("1: MINHEAP\n2: MAXHEAP\n0: EXIT"))

    if s == 1:
        m = int(input("enter the maxsize"))
        minHeap = MinHeap(m)
        while(1):
            s1 = int(input("11: insert\n12: delete\n13: print\n10: exit"))
            if s1 == 11:
                v = int(input("enter value"))
                minHeap.insert(v)
                minHeap.minHeap()
                minHeap.print()
            elif s1 == 12:
                d = minHeap.delete()
                print(d)
                minHeap.print()
            elif s1 == 13:
                minHeap.print()
            elif s1 == 10:
                break
            else:
                print("enter the correct value")
    elif s == 2:
        M = int(input("entr the maxsize"))
        maxHeap = MaxHeap(M)

        while(1):
            s2 = int(input("21: insert\n22: delete\n23: print\n20: exit"))
            if s2 == 21:
                v = int(input("enter the value"))
                maxHeap.insert(v)
                maxHeap.print()
            elif s2 == 22:
                d = maxHeap.delete()
                print(d)
                maxHeap.print()
            elif s2 == 23:
                maxHeap.print()
            elif s2 == 20:
                break
            else:
                print("error enter the correct value")
    elif s == 0:
        exit(0)
    else:
        print("error enter the correct value")