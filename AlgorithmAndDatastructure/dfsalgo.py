def DFS(graph,source,stack=[]):
    # stack=[]
    # if source not in stack:
        stack.append(source)
        if source not in graph:
            return  stack

        # print(stack)
        for neighbour in graph[source]:
            stack=DFS(graph,neighbour,stack)
        return stack


graph = {"A": ["B", "C", "D"],
         "B": ["E"],
         "C": ["F", "G"],
         "D": ["H"],
         "E": ["I"],
         "F": ["J"]}
df=DFS(graph,"A")
print(df)
