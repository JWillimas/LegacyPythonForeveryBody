print("-"*50)#----------------------------------------------

#Question1:Divide-and-Conquer
#Divide:split the big problem into smaller subproblems
#Conquer:solve the small subproblems (often recursively)

print("-"*50)#----------------------------------------------

def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])

    sorted_list=[]
    i=0
    j=0

    while i<len(left) and j<len(right):
        if left[i]<= right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1
    
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


arr= [4, 10, 6, 14, 2, 1, 8, 5]
print(merge_sort(arr))



