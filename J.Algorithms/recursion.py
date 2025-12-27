print("-"*50)#-------------------------------------------------
#Basic case
#divide-and-conquer problems

print("-"*50)#-------------------------------------------------

def countdown(n):
    if n==0:
        print("Done")
        return
    print(n)
    countdown(n-1)

countdown(5)

print("-"*50)#-------------------------------------------------

def factorial(n):
    if n==1:
        print(1)
        return 1
    print(n)
    return n*factorial(n-1)

print(factorial(5))

print("-"*50)#-------------------------------------------------

def sum_list(arr):
    if not arr:
        return 0
    return arr[0]+sum_list(arr[1:])
#arr[1:]means return every thing except first element

arr=[1,2,3,4]

print("-"*50)#-------------------------------------------------

#Tree traversal
#The tree???????

print("-"*50)#-------------------------------------------------