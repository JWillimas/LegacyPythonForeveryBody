#-------------------------------------------------------------
#Question1:
    #Want to understand the linked list
        #Understand the concept of walk through
            #except head the rest element isn't store in memory
            # when we want to get it we just can make it to be the head
            # and read it 
        #Know the object lifetime,instance variables 
            # and when they reset
#-------------------------------------------------------------

class LinkedList:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None
            
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0
    
    def add(self, element):
        node = self.Node(element)
        if self.is_empty():
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.length += 1

    def remove(self, element):
        previous_node = None
        current_node = self.head
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next
        #First circum: there are no certain element
        if current_node is None:
            print("no this element here")
            return        
        
        #Sec circum: the element in the middle
        elif previous_node is not None:
            previous_node.next = current_node.next
        
        #Third circum: element in head 
        else:
            self.head = current_node.next
        self.length -= 1

    def search(self,element):
        node_locate=0
        previous_node=None
        current_node=self.head
        while current_node is not None and current_node.element !=element:
            previous_node = current_node
            current_node = current_node.next
            node_locate+=1
        
        if current_node is None:
            print("no this element here")
            return
        
        else :
            node_locate+=1
            print(f"the first {element} is in the {node_locate} node")
            return 
        
    def get(self,input):
        index=input-1
        if index<0 or index>=self.length:
            raise IndexError("Index out of bounds")
        current_node = self.head
        for _ in range(index):
                current_node=current_node.next
        print(f"the element of index {input} is {current_node.element} ")
        return 



my_list = LinkedList()
print(my_list.is_empty())

my_list.add(1)
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)
my_list.add(5)
my_list.add(3)
my_list.add(2)
my_list.add(3)
my_list.add(4)
my_list.add(5)
my_list.add(1)
my_list.add(2)

my_list.search(5)
my_list.get(1)

print(my_list.is_empty())
print(my_list.length)

my_list = LinkedList()

my_list.add(3)
my_list.add(4)
my_list.add(5)

my_list.remove(1)
my_list.remove(2)

print(my_list.length)
print(my_list.head.next)