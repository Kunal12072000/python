from collections import defaultdict
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

        # Function to print a BFS of graph

    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []


        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
    def DFSutils(self,v,visited):
        visited[v] = True
        print(v, end = " ")
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSutils(i,visited)
    def DFS(self,v):
        visited = [False] * (max(self.graph) +1)
        for i in range(len(self.graph)):
            if visited[i] == False:
                self.DFSutils(i,visited)
    def iscycleutils(self,v,visited,recstack):
        visited[v] = True
        recstack[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                if self.iscycleutils(i,visited,recstack) == True:
                    return True
            elif recstack[i] == True:
                    return True
        recstack[v] = False
        return False

    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False
    def print_graph(self):
        for i in range(len(self.graph)):
            print("Adjancency list of vertex {}\n head".format(i), end="")
            tmp = self.graph[i]
            for j in range(len(self.graph[i])):
                print(" -> {}".format(tmp[j]), end="")

            print(" \n")

# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(4,4)
g.print_graph()

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(0)
print("\n")
g.DFS(2)