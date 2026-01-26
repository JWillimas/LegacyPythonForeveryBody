matrix=[
[0, 1, 0, 0],
[1, 0, 1, 0],
[0, 1, 0, 1],
[0, 0, 1, 0]
]

def dsf(matrix,start):
    node_num=len(matrix)
    visited=set()
    result=[]
    stack=[start]

    while stack:
        node=stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
        
        for neighbor in range(node_num-1,-1,-1):
            if matrix[node][neighbor]==1 and neighbor not in visited:
                stack.append(neighbor)
    return result

print(dsf(matrix,1))

