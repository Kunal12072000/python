class adjNode:
    def __init__(self,data):
        self.data = data
        self.next = None
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [None] * self.V
    def add_edge(self,src,dst):
        node = adjNode(dst)
        node.next = self.graph[src]
        self.graph[src] = node

        node = adjNode(src)
        node.next = self.graph[dst]
        self.graph[dst] = node
    def print_graph(self):
        for i in range(self.V):
            print("Adjancency list of vertex {}\n head".format(i), end="")
            tmp = self.graph[i]
            while tmp:
                print(" -> {}".format(tmp.data), end="")
                tmp = tmp.next
            print(" \n")
    def BFS(self,s):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop()
            tmp = self.graph[s]
            print(s,end = " ")
            while tmp:
                if (visited[tmp.data] == False):

                    queue.append(tmp.data)
                    visited[tmp.data] = True
                    tmp = tmp.next
                else:
                    tmp = tmp.next
if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.print_graph()
    graph.BFS(3)