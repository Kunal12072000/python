import sys
class Graph():
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for i in range(vertices)] for j in range(vertices)]
    def minKey(self,key,mstSet):
        min = int(sys.maxsize)
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return (min_index)
    def primMST(self):
        key = [int(sys.maxsize)] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1
        for c in range(self.V):
            u = self.minKey(key,mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        return(parent)
    def print(self,parent):
        print("Edge \t Weight")
        for i in range(1,self.V):
            print(parent[i],"-",i,"\t",self.graph[i][parent[i]])
print("WE SHOULD ENTER THE GRAPH IN TERMS OF ADJACENCY MATRIX")
n = int(input("enter the number of nodes\n"))
g = Graph(n)
g.graph = []
print("enter lines one by one\n")
for i in range(n):
    g.graph.append(list(map(int,input().split())))

p = g.primMST()
g.print(p)

"""" for the give test case 
    n = 7
0 6 0 4 0 0 0
6 0 7 8 6 0 0
0 7 0 0 4 0 0
4 8 0 0 14 5 0
0 6 4 14 0 7 8
0 0 0 5 7 0 10
0 0 0 0 8 10 0
"""