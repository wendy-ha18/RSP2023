class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # ------ A utility function to add an edge in an undirected graph.
    def addEdge(self, u, v):
    
        self[u].append(v);
        self[v].append(u);
        
    # ------ A utility function to delete an edge in an undirected graph.
    def delEdge(self,  u,  v):
        
        # Traversing through the first vector list
        # and removing the second element from it
        for i in range(len(self[u])):
        
            if (self[u][i] == v):
                
                self[u].pop(i);
                break;
        
        # Traversing through the second vector list
        # and removing the first element from it
        for i in range(len(self[v])):
        
            if (self[v][i] == u):
                
                self[v].pop(i);
                break;
        
    # ------ A utility function to print the selfacency list representation of graph
    def prGraph(self,  V):
        
        for v in range(V):
            
            print("vertex " + str(v), end = ' ')
            
            for x in self[v]:
                print("-> " + str(x), end = '')
                
            print()
        print()