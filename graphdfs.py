import stack

class Graph:
    def __init__(self,n):
        self.n=n
        self.adjacency=[[]for i in range(n)]
        print(self.adjacency)

    def edge(self,node2,node1):
        self.adjacency[node1].append(node2)
        self.adjacency[node2].append(node1)
        print(self.adjacency)

    def dfs(self,source):
        vis=[]
        st=stack.Stack(self.n)
        st.push(source)

        while st.lenth()>0:
            t=st.pop()
            if t not in  vis:
                vis.append(t)
                for k in reversed(self.adjacency[t]):
                    if k not in  vis:
                        st.push(k)
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
Graph1.edge(1,6)
Graph1.edge(6,7)
Graph1.edge(1,7)
print(Graph1.dfs(0))
print(Graph1.adjacency[1])