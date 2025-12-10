print("-"*50+"\n")#----------------------------------------------------

#Buid a class to define shared behavior
    #then create objects that use those behaviors

#recognize the Class as blueprint to Object

#Attribtes are like variables within a class
    #and are used to store data

#Methods are functions defined within a class
    #and are the actions objects created with a calss can perform


class ClassName:
    def __init__(self,name,age):
        #the self(__init__ first object)
             #is alwyas a reference to the specific object
                #being created or used
                     #like example beneath:Object_1,Object_2

        self.name=name
        self.age=age

    def sample_method(self):
        print(self.name.capitalize(),
              self.age.capitalize())

Object_1=ClassName("123","asd")
    #define the first object by the attribute("123","asd")

Object_2=ClassName("456","qwe")
    #definr second Object by second attribute("456","qwe")


Object_1.sample_method()

Object_2.sample_method()

print("-"*50+"\n")#----------------------------------------------------

#Method and Attributes

#instance attribute:
    #unique to each object created from class

#class attribute belong to the class itself 
    #and are shared by all instances of that class.

class   Dog:
    species="French Bulldog"

    def __init__(self,name):
        self.name=name
    
print(Dog.species)

dog1=Dog("Jack")

print(dog1.name)

print(dog1.species)


print("-"*50+"\n")#----------------------------------------------------

class Mat:
    Mat="this is a math function"

    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def sum(self):
        return (self.a+self.b)
    
    def mult(self):
        return (self.a*self.b)
    


Exam01=Mat(1,2)

Exam02=Mat(4,5)

Exam03=Mat(5,6)

print(Exam01.Mat)
print(Exam01.sum())
print(Exam01.mult())
print(type(Exam01.mult))


print("\n")

print(Exam02.Mat)
print(Exam02.sum())
print(Exam02.mult())

print("\n")

print(Exam03.Mat)
print(Exam03.sum())
print(Exam03.mult())





print("-"*50+"\n")#----------------------------------------------------


class Car:
    def __init__(self, color, model):
        self.color = color  # Instance attribute
        self.model = model  # Instance attribute

    def describe(self):
        return (f"This car is {self.color}  {self.model}")

Car_1=Car("red", "Toyota Corolla")
Car_2=Car("green", "Lamborghini Revuelto")

print(Car_1.describe())

print(Car_2.describe())

print("-"*50+"\n")#----------------------------------------------------

print("-"*50+"\n")#----------------------------------------------------

class Menu:
    dish_of_the_day = "spam"

 
print(Menu.dish_of_the_day)