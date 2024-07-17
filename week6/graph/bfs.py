from collections import deque
class graph:
    def __init__(self):
        self.graph={}
    
    def add_edge(self,u,v):
        # add edge from u to v
        if u not in self.graph:
            self.graph[u]=[]
        self.graph[u].append(v)

        # add edge from v to u ( assuming is the graph is unidirectes)
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[v].append(u)

    
    def bfs(self,start):
        visited=set()
        q= deque([start])
        visited.add(start)

        while q:
            v= q.popleft()
            print(v,end='')

            for neighbor in self.graph.get(v,[]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

Graph=graph()

Graph.add_edge('A','B')
Graph.add_edge('A','C')
Graph.add_edge('A','B')
Graph.add_edge('D','B')
Graph.add_edge('C','B')
Graph.add_edge('A','E')


Graph.bfs('A')

    