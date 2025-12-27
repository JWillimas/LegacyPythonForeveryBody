#My solution:
print("-"*50)#---------------------------------------------------------------------------------
def selection_sort(arr):
    for i in range(len(arr)-1) :#len=9,range=[0-8]
        rest_list=arr[i:len(arr)]
        min_rest_list=min(arr[i:len(arr)])#arr[0:9] -->arr[0]---arr[8]
        if arr[i]>min_rest_list:
            index=rest_list.index(min_rest_list)
            arr[i],arr[index+i]=arr[index+i],arr[i]
    return arr

print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))

print("-"*50)#---------------------------------------------------------------------------------






