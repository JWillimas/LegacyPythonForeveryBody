#Prefix attributes with single or double underscore
    #Prefixing a attribute with a double underscore
        #triggers Python's name mangling process,
            #in which Python internally renames the attribute 
                # by adding an underscore 
                    # and the class name as a prefix,turn __attribute 
                        # to _ClassName__attribute
print("*"*50)#------------------------------------------------------------------------


class Example:
    def __init__(self, internal, private):
        self._internal = internal
        self.__private = private

example1 = Example(
    'I can be accessed from outside the class, but should not',
    'I cannot be accessed directly from outside the class'
)

print(example1.__dict__ )
print(example1.__dict__ ["_internal"])
print(example1._Example__private)
    #thought use double underscore to make the __private         #as 
        #as private instance attribute in examlple class
            #but actually it rename it as _Classname__attribute
                #so we can use this outside the class
                    #this is the name mangling

#use the __dict__ special attribute of that instance 
    #which is a dictionary containing the object's attribute


print("*"*50+"\n")#------------------------------------------------------------------------
print("*"*50+"\n")#------------------------------------------------------------------------


class Parent:
    def __init__(self):
        self.name="Parent"
        self.Data="123"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.name="Child"
        self.Data="456"


print(Child().__dict__)
print(Parent().__dict__)
#Because when we use double underscore 
    # it is triggers name mangling execute internally
        #so when we use inheritance and super()
            #the attribute define in parent isn's override

print("*"*50)#------------------------------------------------------------------------
