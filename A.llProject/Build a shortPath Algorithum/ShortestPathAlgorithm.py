#Not space friendly

INF = float('inf')

# adj_matrix = [
#     [0, 5, 3, INF, 11, INF],
#     [5, 0, 1, INF, INF, 2],
#     [3, 1, 0, 1, 5, INF],
#     [INF, INF, 1, 0, 9, 3],
#     [11, INF, 5, 9, 0, INF],
#     [INF, 2, INF, 3, INF, 0],
# ]

adj_matrix=[
    [0,6,2,INF],
    [6,0,3,1],
    [2,3,0,5],
    [INF,1,5,0]
]

def shortest_path(matrix, start_node, target_node=None):
    #Initial the condition we got four list here:
        #matrix,distances,paths,visited
    n = len(matrix)
    distances = [INF] * n #store the distance between now and others
    distances[start_node] = 0 
    paths = [[node_no] for node_no in range(n)]#store the path
    visited = [False] * n #sign the visited

    #fine the min_distance(min_edge) from distances[node_no]
    for _ in range(n):
        min_distance = INF
        current = -1
        for node_no in range(n):
            #if visited[node_no]==False and distance[node_no]<min_distance
            if not visited[node_no] and distances[node_no] < min_distance:
                min_distance = distances[node_no]
                current = node_no

        if current == -1:
            break
        #sign the visted current
        visited[current] = True

            #find the branch and renew the distances-list
        for node_no in range(n):
            distance = matrix[current][node_no]
            if distance != INF and not visited[node_no]:
                new_distance = distances[current] + distance
                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance
                    paths[node_no] = paths[current] + [node_no]

    targets = [target_node] if target_node is not None else range(n)
    
    for node_no in targets:
        if node_no == start_node or distances[node_no] == INF:
            continue
        string_path = (str(n) for n in paths[node_no])
        path = ' -> '.join(string_path)
        print(f'\n{start_node}-{node_no} distance: {distances[node_no]}\nPath: {path}')

    return distances, paths

shortest_path(adj_matrix,0,3)




