#import heap priority queue module
import heapq
 
class Node:
    def __init__(self, v, distance):
        self.v = v
        self.distance = distance
    
    def __lt__(self, other): #compare distance
        return self.distance < other.distance
 

    def dijkstra(V, adj, S):
        visited = [False] * V 
        map = {}
        priority_queue = [] 
        map[S] = Node(S, 0)
        heapq.heappush(priority_queue, Node(S, 0)) 
        
        while priority_queue:
            #pop the node with minimum distance from priority queue
            n = heapq.heappop(priority_queue)
            v = n.v
            distance = n.distance
            visited[v] = True

            adjList = adj[v]

            for edge in adjList:
                if visited[edge[0]] == False:
                    if edge[0] not in map:
                        map[edge[0]] = Node(v, distance + edge[1])
                    else:
                        sn = map[edge[0]]
                        #check if the new distance is less than the current distance of the node
                        if distance + edge[1] < sn.distance:
                            #update the node's distance
                            sn.v = v
                            sn.distance = distance + edge[1]
                    #insert the node to priority queue
                    heapq.heappush(priority_queue, Node(edge[0], distance + edge[1]))
    
        result = [0] * V
        for key in map.keys():
            result[key] = map[key].distance
        return result