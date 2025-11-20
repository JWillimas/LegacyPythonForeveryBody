#1-List:

# developer = ['Alice', 34, 'Rust Developer']
# name,*rest=developer
# #Using Asterisk to store remaining elements 
# #from a list

# print(name)
# print(rest)


# numbers = [1, 2, 3, 4, 5, 6]


# print(numbers[1::3])
# #step interval=3
# #increment=3

#----------------------------------------------------

#2-Common Method use for List

# numbers = [1, 2, 3, 4, 5]
# even_numbers = [6, 8, 10]

# numbers.append(even_numbers)
# #add one list at the end of another

# del numbers[-1]

# print(numbers)


# #if want to add all of the individual numbers
# #from the even_numbers list at the end of the numbers
# numbers = [1, 2, 3, 4, 5]
# even_numbers = [6, 8, 10]

# numbers.extend(even_numbers)

# del numbers[1:4]

# print(numbers)

# developer = ['Alice', 34, 'Rust Developer']

# developer.remove('Alice')
# #Use 'del' to delet the index from list
# #Use 'remove' to remove the element from list
# print(developer)



# numbers = [1, 2, 3, 4, 5]
# numbers.pop(1)

# #pop():remove and return a value

# print(numbers.pop(1))

# programming_languages = ['Rust', 'Java', 'Python', 'C++']
# print(programming_languages.index('Rust'))

# #A tuple is a Python data type used to creat
# #an ordered sequence of values.

# #lists are a mutable data type , tuple are immutable
# #so that it's imposible to remove an item form a tuple

#----------------------------------------------------
#3-Method of tuple
# programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

# print(programming_languages.index('Python') )# 5
# #passing in an optional start index
# #In this example 
# # we are specifying where to start searching for the string

# programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

# print(sorted(programming_languages,reverse=True) )

#----------------------------------------------------
#4-How Do Loops Work?

#Using for Loop to loop through string

# for char in 'code':
#     print(char)

# categories = ['Fruit', 'Vegetable']
# fruits=['Apple','Banana']
# vegetables = ['Carrot']

# for category in categories:
#     if(category=='Fruit'):
#         for fruit in fruits:
#             print(category,fruit)
#     else :
#         for vegetable in vegetables:
#             print(category,vegetable)


# secret_number = 3
# guess = 0

# while guess != secret_number:
#     guess = int(input('Guess the number (1-5): '))
#     # convert the input string into interger with the int()
#     if guess != secret_number:
#         print('Wrong! Try again.')

# print('You got it!')

# developer_names = ['Jess', 'Naomi', 'Tom']

# for developer in developer_names:
#     if developer == 'Naomi':
#         continue
#     #Using 'continue' to skip the current iteration of a Loop
#     #and move onto the next iteration
#     print(developer)


# words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

# for word in words:
#     for letter in word:
#         if letter.lower() in "aeiou":
#             print(f"{word} is vowel word")
#             break
#     else :
#         print(f"{word} is not vowel word")

# for num in range(40, 0, -10):
#     print(num)
#if you wan to generate a sequence of intergers
#in decrementing order ,then you can use a negative 



#----------------------------------------------------
#5-enumerate() and zip()

#The enumerate() function 
# keeps track of the index 
# for an iterable and returns an enumerate object(tuple).



# ZIp() combines lists into pairs of elements 
# and returns an iterator of tuples

#iterate over multiple iterables in parallel?



# languages = ['Spanish', 'English', 'Russian', 'Chinese']

# for language in enumerate(languages):
#     print(language)

# print(type(enumerate(languages)))

# ids = [1, 2, 3, 5]
# developers = ['Naomi', 'Dario', 'Jessica',"",'Tom']

# for inform in zip(ids,developers):
#     print(inform)

#----------------------------------------------------
#6-List Comprehension
#list comprehension allows you to create a new list 
#i a single line by combining a loop and  conditon 
#directly within squae brackets

# even_numbers = []

# for num in range(21):
#     if num % 2 == 0:
#         even_numbers.append(num)

# print(even_numbers)


# even_numbers=[num for num in range(21) if num%2==0]
# print(even_numbers)




# numbers = [1, 2, 3, 4, 5]
# result=[(num,"Even") if num%2==0 else (num,'Odd') for num in numbers ]
# print(result)



#----------------------------------------------------

#filiter function()
#The filter() function is used to select elements 
# from an iterable that meet a specific condition.

# words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

# def is_long_word(word):
#     return len(word) > 4

# long_words = list(filter(is_long_word, words))
# #words as parameters in filiter
# print(long_words)



#Map() function
#which takes an iterable and 
#applies a function to each of its elements.

# celsius = [0, 10, 20, 30, 40]

# def trans(temp):
#     return (temp*9/5)+32

# print(list(map(trans,celsius)))

# [32.0, 50.0, 68.0, 86.0, 104.0]

#sum() function
#This function is used to get the sum 
# from an iterable like a list or tuple.


#------------------------------------------------------------
#Lambda function()
#If you are dealing with a single inline expressions
#then you might consider using a lambda function. 

#anonymous function:lambda functions are anonymous
#so this function no longer has the name square associated with it.

# def square(num):
#     return num**2

# print(square(4))


# print((lambda x : x**2) (4))


#----------------------------------------------------


















#----------------------------------------------------

