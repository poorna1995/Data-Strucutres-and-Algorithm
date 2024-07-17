graph = {
    a=['b','e','f'],
    b=['a','d']
    c=['d','f']
    d=['a','f','g']
    e=[]
    f=[]

}


def breadthFirstSearch(graph,start):
    queue=[start]
    visited=set()
    if start is None:
        return 0
    
    while queue:
        node=queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not visited:
                visited.add(neighbor)
                queue.append(neighbor)
        

