class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dic={}
        for start,end in self.edges:
            if start in self.graph_dic:
                self.graph_dic[start].append(end)
            else:
                self.graph_dic[start]=[end]
    def get_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.graph_dic:
            return []
        paths=[]
        for node in self.graph_dic[start]:
            if node not in path:
                new_paths=self.get_path(node,end,path)
                for p in new_paths:
                    paths.append(p)
        return paths;
    def get_shortest_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return path
        if start not in self.graph_dic:
            return None
        shortest_path=None;
        for node  in self.graph_dic[start]:
            if node not in path:
                sp=self.get_shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path=sp

        return shortest_path



if __name__ == "__main__":
    routes=[("mumbai","paris"),("mumbai","dubai"),("paris","dubai"),("paris","new York"),("dubai","new York"),("new York","toronto")]
    route_graph=Graph(routes)
    print(route_graph.graph_dic)
    start="mumbai"
    end="new York"
    print(route_graph.get_path(start,end))
    print(route_graph.get_shortest_path(start, end))

