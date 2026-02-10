#------------------------------------------------------------------------------

#Q0:Don't mix linked list and BFS!!!
#Q1:What BFS use for ,how to implement it specifily?
#BFS algorithm that 
#visits all neighboring nodes 
#before moving to the next level in the graph
    #It can be used to find the shortest path 
    #between two nodes in an unweighted graph
    #it analyzes all the nodes at each level

#------------------------------------------------------------------------------

from collections import deque
<<<<<<< HEAD
=======

>>>>>>> 088051e24364c927dc5f4fd9fd26cf76fcc9828e
graph={
    "A":["B","C"],
    "B":["D","E"],
    "C":["F","G"],
    "D":[],
    "E":[],
    "F":[],
    "G":[],
}

def bfs(graph,start):

    visited=set()
    queue=deque([start])
    while queue:
        node=queue.popleft()#get the element in ([])(deque)
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in graph[node]:#get the value from graph node
                queue.append(neighbor)

print("-"*50)#------------------------------------------------------------------------------

#Q2:In dict loop,if iterate to a key meet no value
#the function end return

#------------------------------------------------------------------------------
#Recursion Version-----
#------------------------------------------------------------------------------
def dfs_recur(graph, node, visited=set()):
    if node in visited:
        return

    print(node)
    visited.add(node)

    for neighbor in graph[node]:
        dfs_recur(graph, neighbor, visited)
       
#------------------------------------------------------------------------------
#Stacking Version-----
#------------------------------------------------------------------------------
#Q3:for example if i check the B first,how can i make it
#LIFO?In other word, how do i store it reversely?
#------------------------------------------------------------------------------

def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        print(f"{stack}\n")
        node = stack.pop()
        if node not in visited:
            # print(node)
            visited.add(node)
            for neighbor in reversed(graph[node]):
                stack.append(neighbor)

dfs_stack(graph, "A")

