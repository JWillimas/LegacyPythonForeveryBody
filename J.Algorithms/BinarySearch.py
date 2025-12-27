import random

def binary_search_normal(arr,target):
    low=0
    high=len(arr)-1
    Execute_time=0
    while low<=high:
        mid=(high+low)//2
        Execute_time+=1
        if arr[mid]==target:
            return f"\
The target is {target},\n\
the Execute times={Execute_time}\n"
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1

def binary_search_recur(arr,target,low,high,Execute_time=0):
    if low>high:
        return -1
    
    mid=(low+high)//2
    Execute_time+=1

    if arr[mid]==target:
        return f"\
The target is {target},\n\
the Execute times={Execute_time}\n"
    
    elif arr[mid]<target:
        return binary_search_recur(arr,target,mid+1,high)
    else :
        return binary_search_recur(arr,target,low,mid-1)



x=random.randint(1,10)

arr=list(range(1,11))

print(arr)
print(len(arr))

print(binary_search_normal(arr,x))
print(binary_search_recur(arr,x,0,len(arr)))
