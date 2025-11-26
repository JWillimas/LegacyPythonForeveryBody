print("-"*50+"\n")#----------------------------------------------------
print("-"*50+"\n")#----------------------------------------------------
#What are Special Methods 
    #and What Are They Used For?

#Arithmetic operations:
    #addition:__add__()
        #subtraction:__sub__()
            #mutiplication:__mul__()
                #division:__truediv__()

#Normally,Python data types like strings and numbers
    #Are already Know how to add things,do concatenation
        #But when you create your own class
            #python won't konw how to handle things automatically
          
print("-"*50+"\n")#----------------------------------------------------

class Book:
   def __init__(self, title, pages):
       self.title = title
       self.pages = pages

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1.title)) 
print(type(book1)) 
    # TypeError: object of type 'Book' has no len()
        #type(book1)=class '__main__.Book

print(str(book1)) # <__main__.Book object at 0x102ed2900>
#As same as the one below:
print(book1)# <__main__.Book object at 0x102ed2900>


print(book1 == book2) # False even though they have the same number of pages



print("-"*50+"\n")#----------------------------------------------------

class Comic:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages

    def __len__(self):
        return self.pages#int
    
    def __str__(self):
        return self.title#str
    
    def __eq__(self,other):
        return self.title==other.title
    

Marvel=Comic("iron man",444)    
Marvel01=Comic("spider man man",555)    

print(Marvel==Marvel01)

      
print("-"*50+"\n")#----------------------------------------------------


class Cart:
    def __init__(self):
        self.items=[]
        #distinguish the instance attributes
        # def __init__(self,item)   
            #self.item=item it mean assign the item directly
                #Cart01=Cart(5) , Cart01.item=5
        
    def add(self,item):
        self.items.append(item)

    def remove(self,item):
        if item in self.items:
           self.items.remove(item)
        else:
            print(f'{item} is not in cart')

    def __getitem__(self,index):
        #if the object need the item just return it
        return self.items[index]
    
    def __iter__(self):
        #make the object to be iterator
            #return iterator for the container
        return iter(self.items)

    def __contains__(self,item):
        #inspect if item in self and return it
        return item in self.items
    
    #make it clear: Think of special methods as
        #the directors of the activities between a peson
            #programming and the Python language
                #interpreter itself
    


print("-"*50+"\n")#----------------------------------------------------


    
Cart01=Cart()

Cart01.add("Laptop")
Cart01.add("Wireless mouse")
Cart01.add("Ergo")
Cart01.add("keyboard")
Cart01.add("Monitor")

print(Cart01[2])

for item in Cart01:
    print(item)

print("Monitor" in Cart01)


print("-"*50+"\n")#----------------------------------------------------

class Comp:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __gt__(self,other):
        return self.a<other.b
    
Comp01=Comp(1,2)
Comp02=Comp(3,4)

print(Comp01>Comp02)

#the compare magic method is implement
    #in the individual object
        #so got to send  two parameters
            #and it will return the compare outcome
                #in bool form (the compare element is 
                    #define my yourself)











print("-"*50+"\n")#----------------------------------------------------