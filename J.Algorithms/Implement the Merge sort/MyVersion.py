#Divide and Conquer
#Recursion

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left=merge_sort(arr[mid:])
    right=merge_sort(arr[:mid])

    sorted_list=[]
    i=0
    j=0

    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1
        
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

arr=[33,22,33,22]
print(merge_sort(arr))

print("-"*50)#----------------------------------------------------------------
#Divide & Conquer
#Loop Version
#Final result end up inside array
def merg_sort(array):
    if len(array)<=1:
        return 
    
    Mid=len(array)//2

    #Use left_list=merg_sort(array[:Mid])
    #When the Mid=0,this method return None
    #it will cause error
        #Compare with the left_list=array[:Mid] merg_sort(left_list)
        #it would return a error value to left_list,just a empty list
        #Empty list would cause len(list) Error
            #type(list[0])=list
            #type(None)=Nonetype

    left_list=array[:Mid] 
    merg_sort(left_list)  

    right_list=array[Mid:]
    merg_sort(right_list)

    left_index=0
    right_index=0
    sort_index=0

    while left_index<len(left_list) and right_index<len(right_list):
        if left_list[left_index]<=right_list[right_index]:
            array[sort_index]=left_list[left_index]
            left_index+=1
        else:
            array[sort_index]=right_list[right_index]
            right_index+=1
        sort_index+=1

    while left_index<len(left_list):
        array[sort_index]=left_list[left_index]
        left_index+=1
        sort_index+=1
    
    while right_index<len(right_list):
        array[sort_index]=right_list[right_index]
        right_index+=1
        sort_index+=1

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)

    merg_sort(numbers)

    print('Sorted array: ')
    print(numbers)


print("-"*50)#----------------------------------------------------------------