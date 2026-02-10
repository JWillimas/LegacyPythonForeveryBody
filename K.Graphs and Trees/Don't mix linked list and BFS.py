#Q0:If cause AttributeError: 'str' object has no attribute 'next' and no __dict__ for setting new attributes
#it mean i should use the Node class to store the element ,instead of store it to a variable straightly


    #Q1:What BFS use for ,how to implement it specifily?
class Vertexes_list:
    class Node:
        def __init__(self,element):
            self.element=element
            self.next=None
    
    def __init__(self):
        self.head=None
    
    def Is_empty(self):
        return self.head is None

    def add_node(self,arr):
        if arr and self.Is_empty():
            self.head=self.Node(arr[0])
            current_node=self.head
            for i in arr[1:]:
                current_node.next=self.Node(i)
                current_node=current_node.next
    
    def show_node_list(self):
        if not self.Is_empty() :
            current_node=self.head
            show_arr=[]
            while current_node is not None:
                 show_arr.append(current_node.element)
                 current_node=current_node.next
            print(show_arr)
            return

Node_list=Vertexes_list()
vertexes_list=["A","B","C","D"]
Node_list.add_node(vertexes_list)
Node_list.show_node_list()


