import pprint
graph={
    "A":["B","C","D"],
    "B":["A","D"],
    "C":["A"],
    "D":["A"],
    "E":["A"],
    "F":["A"]
}

def trans(graph,input):
    if isinstance(input,str):
        key_num=0
        for key in graph:
            if input==key:
                return key_num
            key_num+=1
    elif isinstance(input,int):
        check_num=0
        for key in graph:
            if check_num==input:
                return key
            check_num+=1

def print_matrix(graph,matrix):
    matrix.append([key for key in graph])
    coloum_node=[]
    for i in range(len(graph.keys())):
        coloum_node.append(matrix[-1][i])
    print(f"   {"  ".join(matrix[-1])}")
    for row in range(len(matrix)-1):
        print(f"{trans(graph,row)} {matrix[row]}") 

def adj_mar(graph):
    vertices=len(graph.keys())
    matrix=[[0]*vertices for _ in range(vertices)]
    for node in graph:
        row=trans(graph,node)
        for neighbor in graph[node]:
            colomn=trans(graph,neighbor)
            matrix[row][colomn]+=1
    print_matrix(graph,matrix)






