adj_matrix=[
 [0, 1, 0, 0],
 [1, 0, 1, 0],
 [0, 1, 0, 1],
 [0, 0, 1, 0]
 ]

result=[]
visited=[]

def dfs(adj_matrix,node):
    elements=len(adj_matrix)
    visited.append(node)
    for n in range(elements):
        if adj_matrix[node][n]==1 and n not in visited :
            dfs(adj_matrix,n)
    result.append(node)
    return visited

dfs(adj_matrix,1)
print(visited)
    


    
