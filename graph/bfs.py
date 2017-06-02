# This will be used for making bfs in the graph.

#Importing defaultdict as this will have added functionalit yon top of default dict
from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        #eg. [('0': [1, 2]), ('1': [2]), ('2': [0, 3]), ('3': [3])]
        self.graph[u].append(v)
        
    def bfs(self, src):
        #Create an array with all False, equals size of graph
        visited = [False] * len(self.graph)
        
        #Initialize an empty queue
        queue = []
        
        #Append src and mark it visited
        queue.append(src)
        visited[src] = True
        
        while queue:
            #dequeue first element and print it, Mark it as Visited.
            s = queue.pop(0)
            print (s)
            
            # Loop over linked elements of dequed element and append it to queue, if not visited. Mark it as Visited
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    
                
if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    # Print the graph
    g.bfs(2)
    