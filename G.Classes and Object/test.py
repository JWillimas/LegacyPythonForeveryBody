# list=["1",'2','3']
# print(len(list))

class Comp:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __len__(self):
        return len(self.b)
    
    def __gt__(self,other):
        return len(self)>len(other)

    
    
Comp01=Comp("20","1")
Comp02=Comp("1","10000")


print(Comp01.a)
print(getattr(Comp01,"a"))

name="123"
planet_type=""
star=""
print("" in (name,planet_type,star))

try:
    if name=="":
        raise ValueError("12")

except ValueError as e:
    raise ValueError("2123132") from e


print("-"*50+"\n")#----------------------------------------------------
print("-"*50+"\n")#----------------------------------------------------


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"

    def __eq__(self, other):
        return self.pages == other.pages

book1 = Book('Built Wealth Like a Boss', 420)
book2 = Book('123', 123)

print(len(book1))        
print(f"{book1}") #eq str(book1)
print(book1==book2)


print("-"*50+"\n")#----------------------------------------------------
print("-"*50+"\n")#----------------------------------------------------



class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')

    def list_items(self):
        return self.items

#Magic Method--Python uses them internally for built-in operations.

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]#use it as index operation

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)

cart = Cart()

cart.add('Laptop')

print(len(cart)) #def __len__(self):

print('Laptop' in cart) # def __contains__(self, item):

print(cart[0]) # def __getitem__(self, index):

for i in cart: # def __iter__(self):
    print(i)

print("-"*50+"\n")#----------------------------------------------------

class Menu: dish_of_the_day = "spam" 

print(Menu.dish_of_the_day) 
#why we can use the class directly?
    #because dish_of_the_day is a class variable
        #and class variable belong to class it self


print("-"*50+"\n")#----------------------------------------------------


