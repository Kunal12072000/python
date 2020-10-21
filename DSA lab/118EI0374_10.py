import sys
import random
class Graph():
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []
    def minDistance(self,d,s):
        mini = int(sys.maxsize)
        min_index = None
        for v in range(self.V):
            if d[v] < mini and s[v] == False:
                mini = d[v]
                min_index = v
        if min_index != None :return min_index
        else:
            for i in range(self.V):
                if s[i] == False:
                    return(i)
    def dijkstra(self,src):
        d = [int(sys.maxsize)] * self.V
        d[src] = 0
        s = [False] * self.V
        for i in range(self.V):
            u = self.minDistance(d,s)

            s[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and s[v] == False and d[v] > d[u] + self.graph[u][v]:
                    d[v] = d[u] + self.graph[u][v]
        return(d)

    def printSolution(self, dist):
        print( "Vertex \tDistance from Source")
        for node in range(self.V):
            print( node, "\t", dist[node])
n = int(input("enter the number of nodes"))
print("NOTES ENTER THE DISTANCE INN FORM OF ADJANCENCY MATRIX")
g = Graph(n)
print("ENTER THE ADJACENCY MATRIX ROW BY ROW")
for i in range(n):
    g.graph.append(list(map(int,input().split())))


'''
n = 7
0 0 2 0 0 0 0
4 0 0 0 0 0 0
0 0 0 0 0 0 0
0 15 0 0 0 5 23
0 17 0 0 0 0 11
0 0 9 0 0 0 13
0 0 0 0 0 0 0
'''
print((g.graph))
for i in range(n):
    print("source is :" ,i)

    d = g.dijkstra(i)
    for i in range(len(d)):
        if d[i] >100000:
            d[i] = 'no path'
    g.printSolution(d)