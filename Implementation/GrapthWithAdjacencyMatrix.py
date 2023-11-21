class Graph: 
     
    # Number of vertices 
    __n = 0
     
    # Adjacency matrix 
    __g = [[0 for x in range(10)] 
              for y in range(10)] 
         
    # Constructor 
    def __init__(self, x): 
        self.__n = x 
     
        # Initializing each element of 
        # the adjacency matrix to zero 
        for i in range(0, self.__n): 
            for j in range(0, self.__n): 
                self.__g[i][j] = 0
                 
    # ------ A function to display adjacency matrix             
    def displayAdjacencyMatrix(self):
         
        # Displaying the 2D matrix 
        for i in range(0, self.__n): 
            print() 
            for j in range(0, self.__n): 
                print("", self.__g[i][j], end = "") 
     
    # ------ A function to update adjacency matrix for edge insertion             
    def addEdge(self, x, y): 
         
        # Checks if the vertices
        # exist in the graph 
        if (x < 0) or (x >= self.__n): 
            print("Vertex {} does not exist!".format(x))
        if (y < 0) or (y >= self.__n): 
            print("Vertex {} does not exist!".format(y))
             
        # Checks if it is a self edge 
        if(x == y): 
            print("Same Vertex!")
 
        else:
             
            # Adding edge between the vertices 
            self.__g[y][x] = 1
            self.__g[x][y] = 1
     
    # ------ A function to update adjacency matrix for edge removal         
    def removeEdge(self, x, y):
         
        # Checks if the vertices
        # exist in the graph 
        if (x < 0) or (x >= self.__n): 
            print("Vertex {} does not exist!".format(x))
        if (y < 0) or (y >= self.__n): 
            print("Vertex {} does not exist!".format(y))
             
        # Checks if it is a self edge 
        if(x == y): 
            print("Same Vertex!")
 
        else:
             
            # Remove edge from between
            # the vertices 
            self.__g[y][x] = 0
            self.__g[x][y] = 0