# def number_pattern(n):
    
#     string=""

#     if not isinstance(n,int):
#         return "Argument must be an integer value."
    
#     if n<1:
#         return "Argument must be an integer greater than 0."

#     else:
#         n+=1
        
#         for i in range(1,n):
#             string+=f"{i} "
            
#     return string

# print(number_pattern(12))
# #-------------------------------------------------

# def number_pattern(n):

#     string=' '
#     if not isinstance(n, int):
#         return "Argument must be an integer value."
    
#     if n < 1:
#         return "Argument must be an integer greater than 0."
    
#     return string.join(str(i) for i in range(1,n+1))

# print(number_pattern(3))

# #-------------------------------------------------

# #generator expression--- (iterable)
##create a sequence of values one at a time
# #each number i in the range convert it to a string
#print((i*2 for i in range(5)))




# print(number_pattern(12))

# def number_pattern(n):
#     numbers = []

#     for i in range(1, n + 1):
#         numbers.append(str(i))  # convert each number to string

#     print(numbers)

#     result = " ".join(numbers)  




#     # join all with a space
#     #join--takes a list/sequence of strings and joins them together
#     return result

# print(type(number_pattern(4)))


# #-------------------------------------------------

# g=(i*2 for i in range(5))

# print(next(g))
