#Object-oriented programming,
    # also known as OOP, 
        #is a programming style in which developers treat everything in their code
            #like a real-world object.

#Four key principles:
#encapsulation, inheritance, polymorphism, and abstraction.


#Prefixing attributes and methods with double underscore
    #effectively prevents them to be accessed from the outside
        #of their class
class Wallet:
   def __init__(self, balance):
       self.__balance = balance # For internal use by convention

   def __validate(self,amount):
       if amount<0:
           raise ValueError('Amount must be positive')

   def deposit(self, amount):
       self.__validate(amount)
       if amount > 0:
           self._balance += amount # Add to the balance safely

   def withdraw(self, amount):
       self.__validate(amount)
       if 0 < amount <= self._balance:
           self._balance -= amount # Remove from the balance safely
    
   def get_balance(self):
       return self.__balance
    
print("*"*50)#------------------------------------------------------------------------

#Getters and Setters:
    #these actions are done through what's known as
        #propertise.They are what connect getters and setters
            #and allow access to data

class Circle:
    def __init__(self,radius):
        self.__radius = radius
    
    @property#getter
    #use @property decorator we can access
        #the method without parentheses(only dot.)
    def radius(self):       #-------And We turn these lines to propeties
        return self.__radius    #---------------------------------------------
    
    #To make a setter create the radius
        #you have to define another method with
            #the same name 
                #and use @<property_name>.setter above it:
    
    #if want to create a propety,and allow to set
        #use @<property_name>.setter as decorator
            #allow unparentheses set the data

    @radius.setter 
    def radius(self, value):  # A setter to set the radius
        if value <= 0:
            raise ValueError('Radius must be positive')
        self.__radius = value

    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self.__radius


my_circle=Circle(100)
my_circle.radius=100# This will call the setter


del my_circle.radius

try :
    print(my_circle.radius)#This will call the getter
except AttributeError as e:
    print("Error:",e)


print("*"*50)#------------------------------------------------------------------------

###Using Attribute to setting propety
    ##Assigns internal variable safely

###don't use propety to setting  value
    #because using self.age in main function means
        #use propety age setter again
            #self.age--------->age(self,value)....


class Person:
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self.age = value   # ❌ WRONG — this calls the setter again!

Person.age=100
print(Person.age)

print("*"*50)#------------------------------------------------------------------------

#Getters let you retrieve a value or even compute a value on the fly.

#Setters let you modify the values safely 
    #by running checks before assignment.

#Properties are what tie these 
    #getters and setters together 
        #so you can write logic while still using dot notation.

#Deleters let you define what happens 
    #when an attribute is deleted.