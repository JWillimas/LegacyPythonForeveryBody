#for space friendly 
    #use link-node to implement the shortest-Path

INF=float("inf")

#neighbor-graph
    #the trail prepare to walk is there
graph={
    "start":{"a":6,"b":2},
    "a":{"fin":1},
    "b":{"a":3,"fin":5},
    "fin":None
}

#cost-graph,already walked
costs={
    "a":6,
    "b":2,
    "fin":INF
}

#parents-graph
parents={
    "a":"start",
    "b":"start",
    "fin":None
}
processed=[]

#def the Dijkstra function

def find_lowest_cost_node(costs):
    lowest_cost=INF
    lowest_cost_node=None
    #Loop through the costs list 
    #and return the miniman key
    for node in costs.keys():
        cost=costs[node]
        if costs[node]<lowest_cost and node not in processed: 
            lowest_cost=costs[node]
            lowest_cost_node=node
    return lowest_cost_node

def Dijkstra_function(graph,costs,parents):
    node=find_lowest_cost_node(costs)
    while node is not None:
        cost=costs[node]
        neighbors=graph[node]
        if neighbors is None:
            break
        for n in neighbors.keys():
            new_cost=cost+neighbors[n]
            if new_cost<costs[n]:
                costs[n]=new_cost
                parents[n]=node
        processed.append(node)
        node=find_lowest_cost_node(costs)
    print(costs["fin"])
    track="->".join(processed)
    print(f"start->{track}->Fin")

Dijkstra_function(graph,costs,parents)

