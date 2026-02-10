matrix=[
[0, 1, 0, 0],
[1, 0, 1, 0],
[0, 1, 0, 1],
[0, 0, 1, 0]
]

def dfs(matrix, start):
    n = len(matrix)
    visited = set()
    result = []
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            result.append(node)

            # Add neighbors in reverse order
                #ensure the order in stack is from large to small
                #so that get the item from the tree in order
            for neighbor in range(n - 1, -1, -1):\
                #matrix[node][neighbor] == 1 means the node and neighbor got a edge
                #neighbor not in visited means that the neighbor is child for node
                if matrix[node][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

    return result

print(dfs(matrix, 1))