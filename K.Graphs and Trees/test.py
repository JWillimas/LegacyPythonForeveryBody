graph={
    "A":["B","C"],
    "B":["D","E"],
    "C":["F","G"],
    "D":[],
    "E":[],
    "F":[],
    "G":[],
}
graph1 = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

def dfs_stack(graph,start_node):
    visited=set()
    stack=[start_node]
    while stack:
        print(stack)
        node=stack.pop()
        if node not in visited:
            visited.add(node)
        for neighbor in reversed(graph[node]):
            stack.append(neighbor)

def binary_recur(arr,target,left=0,right=None):
    if right is None:
        right=len(arr)-1
    
    #base-case!!!!!!
    if left>right:
        print("No target num here")
        return

    mid=(left+right)//2
    
    if target<arr[mid]:
        binary_recur(arr,target,left,mid-1)
    elif target>arr[mid]:
        binary_recur(arr,target,mid+1,right)
    else :
        print(f"the target in the {mid} index")
        return 

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next=None
    
    def show_Tree(self):
        previous=None
        current=root
        current.next=current.left
        while current.next :
            print(f"{current}\n")
            previous=current
            current=current.next
            if current.next==previous.left:
                current.next=previous.right
            










    
root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")

