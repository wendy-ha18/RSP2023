class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # floyd_warshall llgorithm implementation
    nV = 4     # The number of vertices
    INF = 999  # Define Infinity, INF is distance of verticies are not connected with each others.
    def floyd_warshall(self):
        distance = list(map(lambda i: list(map(lambda j: j, i)), self))

        # Choose k is intermediate vertex
        for k in range(nV):
            for i in range(nV):
                for j in range(nV):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        print_solution(distance)


    # Printing the solution
    def print_solution(distance):
        for i in range(nV):
            for j in range(nV):
                if(distance[i][j] == INF):
                    print("INF", end=" ")
                else:
                    print(distance[i][j], end="  ")
            print(" ")