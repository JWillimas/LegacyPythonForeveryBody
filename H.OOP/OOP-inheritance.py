print("*"*50)#------------------------------------------------------------------------

#inheritance:reuse code create clear class hierarchies
#subclass(child class),base class(parent class)

class animal:
    def __init__(self,name):
        self.name=name
    
    @property
    def bark(self):
        return f"{self.name}barking!!!"

class dog(animal):
   @property
   def bark(self):
        base=super().bark
            #Using super()to extend bark function
                #from parent-class instead of re-write it

                    #(This way you can extend the functionality of the parent
                    #  Animals class while still keeping its original beavior)
        return f'{base},woof! woof!! woof!!!'

jack=dog("jacky")
print(jack.bark)

print("*"*50)#------------------------------------------------------------------------

class swim:
    @property
    def swim(self):
        return f"i can swim"

class walk:
    @property
    def walk(self):
        return f"i can walk"

class Amphibian(swim,walk):
    def __init__(self,name):
        self.name=name

    @property
    def Amphibian(self):
        return f"I'm{self.name}i can {self.swim}and{self.walk}"

fog=Amphibian("Fog")
print(fog.Amphibian)

print("*"*50)#------------------------------------------------------------------------

