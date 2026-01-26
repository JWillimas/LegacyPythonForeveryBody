#--------------------------------------------------------------------

#Konwing other trees and it's implement in program
#Q0:What is tree? how do it work?
#Trees = DFS + BFS + structure rules

#Q1:How to implement tries?

#Draw the tree in adjacency-list way

#--------------------------------------------------------------------
#1.Binary Tree:Each node has at most 2 children:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#(My_try): what i want:
#   A
#  B C
#DE FG
class TreeNode:
    class vertex:
        def __init__(self,value):
            self.value=value
    
    def __init__(self):
        self.root=None
        self.left=None
        self.right=None
        self.next=None
        self.height=0

    def is_empty(self):
        return self.root is None
    
    def add(self,value):
        vertex=vertex(value)
        if self.is_empty():
            self.root=vertex
        else:
            current=self.root
            now_height_stay=height-1

            while current.left != None and \
            current.right != None :
                if now_height_stay==height:
                    current.next=current.right
                    height+=1

                current.next=current.left

                if current.next==current.left and \
                    now_height_stay!=height:
                    now_height_stay+=1

            if current.left==None:
                current.left=vertex
            else:
                current.right=vertex

    def show_tree(self):
        if self.is_empty():
            print("No Tree here!")
            return
        else :
            current=self.root
            current.next=current.left
            self.height=0
            now_height_stay=self.height-1

            while current.next!=None:
                if now_height_stay==self.height:
                    print(f"{current.value}\n")
                    current.next=current.right

                print(f"{current.value}")
                current=current.next                             
#Promble:How to loop through a in tree efficiently

#2.Binary Search Tree (BST):
#Rule:Left < Node,Right > Node
#Using recursion method

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = BSTNode(value)
            return
        self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = BSTNode(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = BSTNode(value)
    
bst = BinarySearchTree()
for x in [8, 3, 10, 1, 6]:
    bst.insert(x)

#3.Tree_Traverals(DFS on trees):
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right)

#5.Trie:(autocomplete, dictionary)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
                #If the element No exist in a dict
                #it just create one
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

trie = Trie()
trie.insert("apple")
trie.insert("app")

print(trie.search("app"))    # True
print(trie.search("appl"))   # False

#6.BFS on a tree (level order)
from collections import deque

def bfs(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

#--------------------------------------------------------------------
