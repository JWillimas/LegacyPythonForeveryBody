#First define the INF
#Three way to learn a script:
    #1.give a simple example and run through it
    #2.Know the whole process and function in advance
    #3.keep hand dirty
#--------------------------------------------

INF=float("inf")
adj_matrix=[
    [0,6,2,INF],
    [6,0,3,1],
    [2,3,0,5],
    [INF,1,5,0]
]

#def the Dijkstra function
def Dikstra_function(matrix,start_node,target_node=None):
    #initial parameters:
    n=len(matrix)
    distances=[INF]*n
    distances[start_node]=0
    paths=[[node] for node in range(n)]
    visited=[False]*n
    #Find the min_distance
    for _ in range(n):
        min_distance=INF
        current=-1
        for node in range(n):
            #find out the node not be visited and got min_distance
                #And get to the current node
            if not visited[node] and distances[node]<min_distance:
                min_distance=distances[node]
                current=node
        
        if current==-1:
            break

        visited[current]=True

        #Loop through the neighbor
        for node in range(n):
            distance_betw_node=matrix[current][node]
            if not visited[node] and distance_betw_node!=INF:
                new_distance=distance_betw_node+distances[current]
                if distances[node]>new_distance:
                    distances[node]=new_distance
                    paths[node]=paths[current]+[node]
    
    target=[target_node] if target_node is not None else range(n)
    
    #Get the least cost track and print it
    for node in target:
        if node==start_node or distances[node]==INF:
            continue
        path_string=[str(n) for n in paths[node]] 
        print_path_string="->".join(path_string)
        print(f"the closest distances is:{distances[node]}\n\
the closest path is:{print_path_string}")

Dikstra_function(adj_matrix,0,3)
