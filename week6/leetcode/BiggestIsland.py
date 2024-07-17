graph = {
    'a': ['b', 'e', 'f'],
    'b': ['a', 'd'],
    'c': ['d', 'f'],
    'd': ['a', 'f', 'g'],
    'e': ['b', 'c', 'd'],
    'f': []
}


# def dfs(node):
#     if node is visited:
#         return 0
#     else:
#         visited.add(node)
#         size=1
#         #find neighbor

#         for neighbor in graph[node]:
#             # size =size + dfs(neighbor)
#             size+=dfs(neighbor)

#         return size

def dfs(node, graph, visited):
    if node in visited:
        return 0
    visited.add(node)
    size = 1
    for neighbor in graph.get(node, []):
        size += dfs(neighbor, graph, visited)
    return size






def biggestIsland(graph):
    visited=set()
    largest=0
# iterate over graph
    for node in graph:
        if node not in visited:
            componentSize=dfs(node, graph, visited)
            if (componentSize>largest):
                largest=componentSize
    return largest



print(biggestIsland(graph))


