#With polymorphism you have access to an interface 
    #where  you can interact with many objects of the same kind

#Polymorphism allows methods in different classes to share 
    # the same name but perform different tasks


print("*"*50)#------------------------------------------------------------------------

class Cat:
    def speak(self):
        return "cat meow meow"

class Dog:
    def speak(self):
        return "dog wow wow"

class Lizer:
    def speak(self):
        return "Lizer zizi"

def animal_sound(animal):
    print(animal.speak())

animal_sound(Cat())
    #class+parathesis=create a object
        #only Cat mean class,but class is a blue print
            #not a object

animal_sound(Dog())
animal_sound(Lizer())




print("*"*50)#------------------------------------------------------------------------

class Twitter:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"🐦 Tweet: '{self.content}' (280 chars max)"

class Instagram:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"📸 Instagram Post: '{self.content}' + ✨ filters"

class LinkedIn:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"💼 LinkedIn Article: '{self.content}' (Professional Mode)"

def start(social_media):
   print(social_media.post())  # Calls .post() on any object

# Instances
tweet = Twitter('Just learned Python polymorphism!')
photo = Instagram('Sunset vibes 🌅')
article = LinkedIn('Why OOP matters in 2024')

start(tweet)
start(photo)
start(article)


print("*"*50)#------------------------------------------------------------------------

class Animal:
   def speak(self):
       return 'Some generic sound'

class Cat(Animal):
   def speak(self):
       return 'A cat meow'

class Dog(Animal):
   def speak(self):
       return 'A dog barks woof woof'

class Monkey(Animal):
   def speak(self):
       return 'A monkey ooh ooh aah aah ooh ooh aah aah'

animal=[Animal(),Cat(),Dog(),Monkey()]
for animal_sound in animal:
    print(animal_sound.speak())

print("*"*50)#------------------------------------------------------------------------









print("*"*50)#------------------------------------------------------------------------