import numpy as np
#Minimum span tree using Prims
  
""" 
            100
       (0)------->(3) 
        |         /|\ 
      15|          | 
        |         5| 5 
       \|/        \|/ 
       (1)------->(2) 
            3           """
#Disconnected edges have infinite weight
            
#Class to represent a graph 
class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = [] # default dictionary  
                                # to store graph 
          
   
    # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 
        
g = Graph(4)
# Insert any graph here 
#Pattern is (i,j,weight) 
g.addEdge(0, 3, 100) 
g.addEdge(0, 1, 15) 
g.addEdge(1, 2, 3) 
g.addEdge(2, 3, 5) 
g.addEdge(3, 2, 5) 
input=g.graph

#Graph constructed so now we transform it to a more user friendly(array) form to represent a directed graph
graph=np.ones((4,4))*np.inf
for ip in input:
    graph[ip[0]][ip[1]]=ip[2]
    graph[ip[1]][ip[0]]=ip[2]#Since undirected graph
for i in range(4):
    graph[i][i]=0
V=len(graph)
  
#Key values used to pick minimum weight edge in cut 
key = [np.inf] * V 
parent = [None] * V # Array to store constructed MST 
key[0] = 0 
mstSet = [False] * V 
parent[0] = -1 # First node is always the root of 

for vert in range(V): 
    min = np.inf 
  
    for v in range(V): 
        if key[v] < min and mstSet[v] == False: 
            min = key[v] 
            min_index = v 
    u = min_index
    mstSet[u] = True
    for v in range(V): 
        if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]: 
            key[v] = graph[u][v] 
            parent[v] = u 
print ("Edge \tWeight")
for i in range(1,V): 
    print (parent[i],"-",i,"\t",graph[i][ parent[i] ])