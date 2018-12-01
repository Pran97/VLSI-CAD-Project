import numpy as np
#Floyd Algo for finding shortest between every nodes in a graph O(N^3) time complexity, O(N^2) space complexity
  
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
for i in range(4):
    graph[i][i]=0
'''
graph = [[0,15,np.inf,100], 
             [np.inf,0,3,np.inf], 
             [np.inf, np.inf, 0,  5], 
             [np.inf, np.inf,5 , 0] ] 

graph= [[0, 3, 3, 3, 5, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
          [np.inf, 0, np.inf, np.inf, np.inf, 3, np.inf, 2, np.inf, np.inf, np.inf, np.inf, np.inf],
          [np.inf, np.inf, 0, np.inf, np.inf, 3, 2, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
          [np.inf, np.inf, np.inf, 0, np.inf, 1, np.inf, 2, np.inf, np.inf, np.inf, np.inf, np.inf],
          [np.inf, np.inf, np.inf, np.inf, 0, np.inf, 2, 2, np.inf, np.inf, np.inf, np.inf, np.inf],
          [np.inf, np.inf, np.inf, np.inf, np.inf, 0, np.inf, np.inf, 5, 2, np.inf, np.inf, np.inf],
          [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0, np.inf, 1, np.inf, 1, 2, np.inf],
          [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0, np.inf, 2, 1, 2, np.inf],
          [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0, np.inf, np.inf, np.inf, 6],
          [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0, np.inf, np.inf, 3],
          [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0, np.inf, 3],
          [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0, 2],
          [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0]]
'''

V =len(graph)
  
  
for k in range(V): 
    for i in range(V): 
        for j in range(V):
            
            #We are checking if k lies in the shortest path b/w i and j, so update only if path joing i to k and k to  j
            #is shorter than current path b/w i and j
            if(graph[i][k]+ graph[k][j] < graph[i][j]):
                graph[i][j]=graph[i][k]+ graph[k][j]
            else:
                
                graph[i][j] = graph[i][j]
  
    print('The graph in '+str(k)+"th step \n"+str(np.array(graph)))