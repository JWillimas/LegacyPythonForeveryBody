test_line="This is Test line"

def reverse(line):
    return "".join(reversed(line))

print(reverse(test_line))

print("-"*50)#---------------------------------------------------------------

test_list=["original"]
test_list.append("Test stacking process")#push this Last-in Satck
print(test_list.pop())#pop out the last form stack

print("-"*50)#---------------------------------------------------------------

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next=node2
node2.next=node3

current=node1
while current:
    print(current.data)
    current=current.next

print("-"*50)#---------------------------------------------------------------

test_set={2,5,5,5,6,7}
print(5 in test_set )
print(test_set)

print("-"*50)#---------------------------------------------------------------
numbers = [2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers.pop())

unique_numlist=list(unique_numbers)
print(unique_numlist)

print("-"*50)#---------------------------------------------------------------

set_a = {1, 2, 3, 4}
set_b = {1,2, 3, 4, 5, 6}


print(set_a.difference(set_b))
print(set_a.symmetric_difference(set_b))
print(set_a.issubset(set_b))

print("-"*50)#---------------------------------------------------------------