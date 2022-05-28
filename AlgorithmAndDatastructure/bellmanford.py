class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]
    def add_edge(self,s,d,w):
        self.graph.append([s,d,w])
    def print_solution(self,dist):
        print("Vertex distance from Source")
        for i in range(self.V):
            print("{0}\t \t {1}".format(i,dist[i]))
    def bellman_ford(self,src):
        dist=[float("Inf")]*self.V
        dist[src]=0
        for _ in range(self.V-1):
            for s,d,w in self.graph:
                if dist[s] !=float("Inf") and dist[s]+w<dist[d]:
                    dist[d]=dist[s]+w
        for s,d,w in self.graph:
            if dist[s] !=float("Inf") and dist[s]+w<dist[d]:
                print("Graph contains negative cycle")
                return
        self.print_solution((dist))
g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 2)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 3)
g.add_edge(1, 2, 3)
g.add_edge(2, 1, 1)
g.add_edge(2, 3, 4)
g.add_edge(2, 4, 5)
g.add_edge(4, 3, -5)

g.bellman_ford(0)