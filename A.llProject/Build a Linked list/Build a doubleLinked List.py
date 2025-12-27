
class LinkedList:
    class Node:
        def __init__(self,element):
            self.element=element
            self.next=None
            self.last=None

    def __init__(self):
        self.list_length=0
        self.head=None
        self.tail=None

    
    def is_empty(self):
        return self.list_length==0
    
    def add(self,element,locate):
        node = self.Node(element)
        if self.is_empty() and locate=="head":
            self.head = node
        elif self.is_empty() and locate=="tail":
            self.tail = node
        else:
            if locate=="head":
                current_node = self.head
                while current_node.next is not None:
                    current_node = current_node.next
                self.tail = node
                current_node.next = self.tail

            elif locate=="tail":
                current_node=self.tail
                while current_node.last is not None:
                    current_node = current_node.last
                self.head= node
                current_node.last = self.head

        self.list_length += 1


    def remove(self,element):
        current_node=self.head
        previous_node=None
        while current_node.next is not None and current_node.element !=element:
            previous_node=current_node
            current_node=current_node.next

        if current_node.element is None:
            print("There are no element here")
            return
        
        elif previous_node is not None:
            previous_node.next=current_node.next

        else:
            self.head=current_node.next
        self.list_length -= 1
    
    def get_list_element(self):
        return f"There are {self.list_length} elements here"



my_list=LinkedList()
my_list.add(1,"head")
my_list.add(2,"head")
my_list.add(3,"head")

print(my_list.head.element)

        
