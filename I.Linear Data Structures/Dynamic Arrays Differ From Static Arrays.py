#Static arrays  have a fixed size
#They store elements in adjacent memory locations
    #However this data structure cannot grow or shrink
    #so if number of elements that wll be stored can vary
    #you should use a dynamic array instead

#Trying to increase the size of a static array would involve
#creating a new array and copying all the elements
#from the old array to a new one,which is inefficient.

#Dynamic array:more flexible ,can grow and shrink automatically
#while the program is running

#Accessing elements of daynamic array takes constant time O(1)
# Inserting an element in middle takes linear time O(n)
    #because all the elements need to be relocated

#Python's built-in list data structure works as a dynamic array
