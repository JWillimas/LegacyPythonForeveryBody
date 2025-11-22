
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

# iterate over all the values of the dictionary 
for product,price in products.items():
    products[product]=round(price*0.8)

#Unpacking the dict and process the value saperately
#And store it by the new key

print(products)

print("-"*50,"\n")#-----------------------------------------------------
# iterate over the key-value pairs 
# while keeping track of a counter

for i in enumerate(products):
    print(i)

print(enumerate(products))

print("\n")

for i in enumerate(products.keys()):
    print(i)

print(enumerate(products))


print("\n")

for counter,product in enumerate(products.items()):
    
    print(counter)



print("-"*50,"\n")#-----------------------------------------------------
