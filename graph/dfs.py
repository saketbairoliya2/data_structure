# Code for dfs.

from collections import defaultdict

class Graph:
    
    #Initialize with dict
    def __init__(self):
        #self.graph = []
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        #eg. [('0': [1, 2]), ('1': [2]), ('2': [0, 3]), ('3': [3])]
        self.graph[u].append(v)
        
    def dfsUtil(self, visited, src):
        
        # Mark the current node as visited node and print it.
        visited[src] = True
        print src
        
        # Loop over all the adjecent nodes and call function recursively
        for i in self.graph[src]:
            if visited[i] == False:
                self.dfsUtil(visited, i)
        
        
    def dfs(self, src):
        
        #Mark a visited array with False
        visited = [False] * len(self.graph)
        
        #call util for recursive traversal
        self.dfsUtil(visited, src)
            

if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    #Do dfs and print elements
    g.dfs(2)