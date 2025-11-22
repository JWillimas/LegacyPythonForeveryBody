#dictionary---store collections of key-value pairs.
#you use a key to find its corresponding value.

pizza = dict([('name', 'Margherita Pizza')
              , ('price', 8.9),
                ('calories_per_slice', 250), 
                ('toppings', ['mozzarella', 'basil'])])

#list consist of tuple , be pass to dict() as argument
#these tuple contain the key as the first element

pizza['flavor']="sour"
#If the key doesn't exist in the dictionary
#a new key-value pair will be created. 

print(pizza)

print("-"*50,"\n")#-----------------------------------------------------


#Dictionaries helpful method:
pizza.get('toppings', [])
#If "toppings" does exist it return the value
#if not return empty list

print(pizza.get("flavor"))

print(pizza.keys(),"\n")

print(pizza.values(),"\n")

print(pizza.items(),"\n")

#just return a view object 
#with all the keys and values in the dictionary

#A view object is just a way 
#to see the content of a dictionary
#without creating a separate copy of the data.

pizza['woulditpop']="y/n"

print(pizza,"\n")

print(pizza.popitem(),"\n")

print(pizza,"\n")


print("-"*50,"\n")#-----------------------------------------------------

pizza.update({"price":15,"total_time":25})

print(pizza)

print("-"*50,"\n")#-----------------------------------------------------
