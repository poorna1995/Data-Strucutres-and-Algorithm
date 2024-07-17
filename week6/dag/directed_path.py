# gieven two nodes (start,destination) in a directed acyclic graph (DAG) . return true if there is a directed path from start to destination otherwise return false



# eg:1

# input:start =>1 destination=>10

# output=true
# expalination : there is directed path




graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [4, 2, 1],
    4: [2, 1],
    5: [1, 8]
}

start=1
dest=5
# Check the start is not none=> loop until stack is 0 => pop value in the stack => check of the value is 
# visited if not add into the visited => take all the neighbor of the visited element => add to the stack => 

def dfs(graph,start,dest):
    stack=[start]
    visited=set()
    if start is None:
        return 0
    while stack:
        node =stack.pop()
        if node == dest:
            return True
        if node not in visited:
            visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                stack.append(neighbor)
    return False


# Destination= dfs(graph,start,dest)
print(dfs(graph,start,dest))








# def DAG(graph,start,dest):
#     stack=[start]
#     visited=set()

#     if start is None:
#         return 0
#     while stack:
#         node=stack.pop()
#         if node == dest:
#             return True
#         if node not visited:
#             visited.add(node)
#         for neighbor in graph[node]:
#             stack.append(neighbor)
#     return False



# def BFS(graph,start,dest):
#     visited=set()
#     queue=[start]

#      if start is None:
#         return 0
    
#     while queue:
#         node=queue.pop(0)
#         if node == dest:
#             return True
#         if node not visited:
#             visited.add(node)
#         for neighbor in graph[node]:
#             queue.append(neighbor)
#     return False



# def hasPathRecur(graph,start,dest):
#     visited=set()
#     if start == dest:
#         return True
#     if start not visited:
#         return false
#     visited.add(start)
#     for neighbor in graph[start]:
#         if hasPathRecur(graph,neighbor,dest) == True:
#             return True
#     return False
        


