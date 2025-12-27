class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"


points=[Point(1,2),12]

print(points)

print("-"*50)#--------------------------------------------------------

class Parent:
    def __init__(self):
        self.__data = 'Parent data'

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = 'Child data'

p=Parent()
c = Child()

print(p.__dict__)
print(c.__dict__)

print("-"*50)#--------------------------------------------------------