print("*"*50)#------------------------------------------------------------------------

#Abstraction is the process of hiding complex implementation details 
    #and showing only the essential features of an object or system. 

#how Python implements abstraction
    #it does so through the abc module
        #this module provides the ABC class
            #and the @abstractmethod decorator.
                # (standing for "abstract base class")

from abc import ABC, abstractmethod

# The blueprint for any toy that can speak
    #The class ABC and abtractmethod defind the method
        #Then we can use the class contain TalkingToy as blue print
            #And the TalkingToy isn't create a TalkingToy instance
            #TalkingToy(ABC) NOT required to implement speak()
                #but 
class TalkingToy(ABC):
   def __init__(self, name):
       self.name = name
   @abstractmethod
   def speak(self):
       pass

class RobotToy(TalkingToy):
   def speak(self):
       print(f'{self.name} says beep boop! I am a robot!')

class TeddyBearToy(TalkingToy):
   def speak(self):
       print(f"{self.name} says hug me! I'm cuddly!")

class DinosaurToy(TalkingToy):
   def speak(self):
       print(f'{self.name} says ROOOOAR!')

# Create toys
rusty = RobotToy('Rusty')
fluffy = TeddyBearToy('Fluffy')
rex = DinosaurToy('Rex')

toys = [rusty, fluffy, rex]
for toy in toys:
   toy.speak()

# Output:
# Rusty says beep boop! I am a robot!
# Fluffy says hug me! I'm cuddly!
# Rex says ROOOOAR!


print("*"*50)#------------------------------------------------------------------------
