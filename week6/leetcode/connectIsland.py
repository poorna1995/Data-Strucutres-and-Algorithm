graph = {
    'a': ['b', 'e', 'f'],
    'b': ['a', 'd'],
    'c': ['d', 'f'],
    'd': ['a', 'f', 'g'],
    'e': ['b', 'c', 'd'],
    'f': []
}



# Loop the values in the garph, chec the value is in the visited then do the dfs => then increase the count 

def dfs(node,graph,visited):
    if node not in visited:
        visited.add(node)
        for neighbor in graph.get(node,[]):
                dfs(neighbor,graph,visited)

def connectedIsland(graph):
    visited=set()
    count=0
    for node in graph:
        if node not in visited:
            dfs(node, graph,visited)
            count+=1
    return count


print(connectedIsland(graph))


