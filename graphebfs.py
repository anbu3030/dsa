import Queue1

class Graph:
    def __init__(self,n):
        self.n=n
        self.adjacency=[[]for i in range(n)]
        print(self.adjacency)

    def edge(self,node2,node1):
        self.adjacency[node1].append(node2)
        self.adjacency[node2].append(node1)
        print(self.adjacency)

    def bfs(self,source):
        vis=[]
        Qu=Queue1.Queue(self.n)
        vis.append(source)
        Qu.enqueue(source)
        while Qu.lenth()>0:
            d=Qu.dequeue()

            for s in self.adjacency[d]:
                if s not in vis:
                    vis.append(s)
                    Qu.enqueue(s)
        return vis

Graph1=Graph(8)
Graph1.edge(0,1)
Graph1.edge(1,2)
Graph1.edge(2,3)
Graph1.edge(1,3)
Graph1.edge(3,4)
Graph1.edge(1,4)
Graph1.edge(4,5)
Graph1.edge(1,5)
Graph1.edge(5,6)
Graph1.edge(6,7)
print(Graph1.bfs(0))
