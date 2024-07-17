graph = {
    a=['b','e','f'],
    b=['a','d']
    c=['d','f']
    d=['a','f','g']
    e=[]
    f=[]

}

def depthFirstSearch(graph,start):
    stack=[start]
    visited=set()

    if start is None:
        return 0
    while stack:
        node=stack.pop()
        if node is not visited:
            visited.add(node)
        for neighbor in graph[node]:
            if neighbor is not visited:
                stack.append(neighbor)
    return visited


def dfsRecursion(graph,start):
    visited=set()
    if start is not visited:
        visited.add(start)
        for neighbor in graph[start]:
            dfsRecursion(graph,neighbor,visited)
    return visited
        




