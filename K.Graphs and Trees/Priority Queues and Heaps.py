#Q0:confuse about the relationship
#between array and heap

#what is array?
#why heaps are typically 
#implemented as arrays in practice

#why:Arrays simplify the logic 
#for accessing parent and child nodes
#using mathematical formulas.


#Q1:how to implement heap paratically(in code)

#Q2:why The average and worst case time complexities 
#for inserting and extracting 
#the minimum or maximum value from a heap 
#(depending on the type of heap) 
#are logarithmic O(log n)

#Q3:implement The "heapify" operation,
#where the heap is built from an unsorted list


import heapq

my_heap=[]
heapq.heappush(my_heap,9)
print(heapq.heappop(my_heap))

heapq.heappush(my_heap,(2,3))
heapq.heappush(my_heap,(1,2))
heapq.heappush(my_heap,(0,0,-2))
heapq.heappush(my_heap,(0,1,-3))


print(heapq.heappop(my_heap))
print(heapq.heappop(my_heap))