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

name=""
planet_type=""
star=""
print("" in (name,planet_type,star))

try:
    if name=="":
        raise ValueError("12")

except ValueError as e:
    raise ValueError("2123132") from e

