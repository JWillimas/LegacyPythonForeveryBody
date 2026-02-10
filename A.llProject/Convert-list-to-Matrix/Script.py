#Warning:
    #in pyton there is a mistake here:
    #we create a Matrix in this way: Matrix=[[0]*num]*num
    #it means copy the [0]*num in num times 
    #if check the address in each row ,it would be the same 

#------------------------------------------------------------
adjacency_list={
    0: [2],
    1: [2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

def adjacency_list_to_matrix(adj_list):
    num=len(adj_list)
    #inital_Matrix:Using iterable and comprehension way
    Matrix=[[0 for _ in range(num)]for _ in range(num)]
    #row---horizonal
    for row in range(num):
        #Loop through the node's neihbor in list
        for node in adj_list[row]:
            #column--vertical
            for column in range(num):
                if node==column:
                    Matrix[row][column]=1
                
    print(num)
    print(Matrix)

adjacency_list_to_matrix(adjacency_list)