class Graph:
    def __init__(self,n):
        self.n=n
        self.adjacency=[[]for i in range(n)]
        print(self.adjacency)

    def edge(self,node2,node1):
        self.adjacency[node1].append(node2)
        self.adjacency[node2].append(node1)
        print(self.adjacency)

Graph1=Graph(5)
Graph1.edge(0,1)
Graph1.edge(0,2)
Graph1.edge(1,2)
Graph1.edge(1,3)
Graph1.edge(4,1)