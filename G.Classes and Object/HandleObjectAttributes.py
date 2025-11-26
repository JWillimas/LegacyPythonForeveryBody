print("-"*50+"\n")#----------------------------------------------------
print("-"*50+"\n")#----------------------------------------------------

# Handle Object Attributes Dynamically
    #getattr()-makes it possible to read an attribute 
        # from an object
        #syntax: getattr(object,atrribute_name,default_value)


class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

person00=Person("John",44)

attr_name=input('Enter the attribute you want to see: ')
print(getattr(person00 , attr_name , 'Attribute not found'))
    #When you use getattr()
        #you don't have to assinged the attrs in code first


print("-"*50+"\n")#----------------------------------------------------


person = Person('John Doe', 30) 

inform=[]

#the build-in dir() function lets you look through
            #all attribute names on the objects

for attr in dir(person):
    if not attr.startswith('__') and \
        not callable(getattr(person,attr)):
# Ignore dunder methods like __init__ or __str__
    #Ignore regular methods

            value=getattr(person,attr)
            inform.append(f"{attr}:{value}")

print(sorted(inform,reverse=True))


print("-"*50+"\n")#----------------------------------------------------

        #setattr()-lets you  creat your attribute
            #or undate your existing one dynamically
        #syntax(object, attribute_name, value)

class Configuration:
     pass

settings_data={
     'server_url':'https://api.example.com',
     'timeout_sec':30,
     'max_retries':5
}

config_obj=Configuration()

for attr_name,attr_value in settings_data.items():
     setattr(config_obj,attr_name,attr_value)
    
for attr in dir(config_obj):
    if not attr.startswith('__') and \
        not callable(getattr(config_obj,attr)):
            value=getattr(config_obj,attr)
            print(f"{attr}:{value}") 
         


print("-"*50+"\n")#----------------------------------------------------
    #hasattr()-check is a attributes exist?
        #and return True or False

    #syntax-hasattr(object,attribute_name):
print(hasattr(config_obj, 'max_retries'))



print("-"*50+"\n")#----------------------------------------------------
    #delattr()-lets you remove an attribute dynamically
        #syntax:delattr(object,attribute_name)


del_data={
     'timeout_sec':30,
     'max_retries':5
}
for attr in dir(config_obj):
    if not attr.startswith('__') and \
    not callable(getattr(config_obj,attr)):
            value=getattr(config_obj,attr)
            print(f"{attr}:{value}\nif exist?")

            if attr in del_data:
                delattr(config_obj,attr)

            print(hasattr(config_obj,attr),"\n")
  
print("-"*50+"\n")#----------------------------------------------------

