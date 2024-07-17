edges=[
    ['b','a'],
    ['c','a'],
    ['b','c'],
    ['q','r'],
    ['q','s'],
    ['q','u'],
    ['q','t']

]

# [b,a]
# graph=[
#     a:['b','c','e']
# ]

# Loop =>  check if doesn't exist, then add ey => push both

def convertGraph(edges):
    graph={}
    for edge in edges:
        a,b=edge
        if a not in graph:
            graph[a]=[]
        
        if b not in graph:
            graph[b]=[]
        
        graph[a].append(b)
        graph[b].append(a)
    return graph






# def convertGraph(edges):
#     graph={} # a:[] ,b:[]
#     for edge in edges: # ['b','a']
#         [a,b]=edge
#         if a not in graph:
#             graph[a]=[]
#         if b not in graph:
#             graph[b]=[]
        
#         graph[a].append(b)
#         graph[b].append(a)
#     return graph


        
      
graph = convertGraph(edges)
print(graph)