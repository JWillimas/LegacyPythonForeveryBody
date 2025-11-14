#Escape the single or double quotation mark---------------->
#in the string with a backslash (\). 
# With this method
#  you can use either single or double quotation marks to 
# wrap the string itself:
quote="She said ,\"hellow\""
print(quote)

#MultiLine---------------->
my_str_3="""Multiline
string"""
print(my_str_3)

my_str_4="""
Another
multiline
string
"""
print(my_str_4)


#"[]"square brackets---------------->
#Work with string---------------->

my_str=' hellow wrold '
trimed_my_str=my_str.strip()
print(trimed_my_str)

Switched_my_str=my_str.replace('hellow','hi')
print(Switched_my_str)

my_str = 'hello world'

split_words = my_str.split()
print(type(split_words))

find_str=my_str.find('o')
print(find_str)

#Floor division operator'//(forward slash)'---cpar---modulo operator%(reminder)


#bitwise operator:
greet = 2 #010
greet &= 3 #011
print(greet)    # 010&011=010(binary)=2(dec)
print(f'\n')    # 010&011=010(binary)=2(dec)


#>>This shifts the bits to the right by n positions.
a=8 #1000
a>>=2 #0010
print(a)


#Enclosing scope:
def outer_func():
    mag="Hellow there !"
    res=""
    def inner_func(): #Enclose Function
        nonlocal res 
        #nonlocal :Allow modification of 
        # an enclosing variable
        
        res="how are you"
        
        print(mag)
    
    inner_func()
    print(res)

outer_func()

print(f'\n') 

#------------------>>>

my_var_1 = 7

def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)

show_vars() # 7 10

# my_var_2 is now a global variable and can be accessed anywhere in the program
print(my_var_2)

#------------------>>>
#Short-circuiting operation:
# python checks values from left to right 
# and stops as soon as it determines the final result



