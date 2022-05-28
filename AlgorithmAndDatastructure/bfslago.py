def BFS(grap,source):
    queue=[]
    visited=[]
    queue.append(source)
    visited.append(source)
    while queue:
        node=queue.pop(0)
        print('visited node =>',node)
        for edge in grap[node]:
            if  edge not in visited:
                queue.append(edge)
                visited.append(edge)


graps={1:[2,3],2:[4,5],3:[6],4:[],5:[6],6:[]}
BFS(graps,1)