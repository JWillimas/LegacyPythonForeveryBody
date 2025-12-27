#Version1:------------------------------------------------------------
def quick_sort(arr):
    if len(arr)<=1:
        return arr

    pivot=arr[0]
    result=[]
    less=[x for x in arr if x<pivot]
    equal=[ x for x in arr if x==pivot]
    greater=[x for x in arr if x>pivot ]
    result=quick_sort(less)+equal+quick_sort(greater)
    return result

print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))

