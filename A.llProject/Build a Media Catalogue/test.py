test=" "

if not test.strip():
    print(1)
else : print(2)

def test01():
    """this is test01"""
    return"1213"

def test02():
    return"""
This is line one
This is line two
This is line three
"""

print(test01())
print(test01.__doc__)


class test_Parent:
    def __str__(self):
        return "Parent" 

class test_Chid(test_Parent):
    def __str__(self):
        return "Chid" 

print(test_Parent())


print(type(test_Parent())==test_Parent)

print(type(test_Chid())==test_Parent)

