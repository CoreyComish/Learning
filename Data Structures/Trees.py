# Purpose: Learn and provide examples of Trees

# What is a Tree?
"""
Data structure that represents a dynamic set of data
Non-Linear
A connected, undirected graph with no cycles
A collection of nodes, connected by edges, hierarchial relationship between nodes
Many different types of trees, but they all contain the following properties:
Root = The beggining node, Level 0
Branches/Edge = Connection between nodes, usually two per node
Leafs = The last nodes in the tree
Parent = Node that is one level above and connected by an edge
Child = Node that is one level below and connected by an edge
Sibilings = Node that is on the same level, connected by the other edge of parent
"""

# What are some different types of trees?
"""
Binary Tree
    A tree in which each parent has at most 2 children
Binary Search Tree
    Left subtree of a node contains only nodes with keys lesser than the nodes key
    Right subtree of a node contains only nodes with keys greater than nodes key
    Left and right subtree are also binary search trees
    Two branches per node, max
AVL Tree
    A self balancing Binary Search Tree
    Difference between heights of left and right subtrees for any node cant be > 1
Red-Black Tree
    Self balancing Binary Search Tree
    Each node has an extra bit, often interpreted as red or black
    These colors help ensure that the tree remains balanced
... and many more
"""

# What are the different ways we can traverse a tree?
"""
Pre-Order:
    1) Visit Node
    2) Traverse Left Subtree
    3) Traverse Right Subtree
In-Order:
    1) Traverse Left Subtree
    2) Visit Node
    3) Travers Right Subtree
Post-Order:
    1) Traverse Left Subtree
    2) Traverse Right Subtree
    3) Visit Node
Level-Order:
    Traverses and Visits nodes level by level, left to right

Pre-Order, In-Order, Post-Order are Depth First and can implemented using a Stack
Level Order is Breadth First and can be implemented using a Queue
"""

# What are trees useful for?
"""
Commonly used to represent or manipulate hierarchial data
    File Systems
    Directory Structure
Machine Learning
Chess Game to store defense moves of player
Decision Trees
Searching and Sorting
"""

# Binary Search Tree Opertations and Space
"""
Access: O(log n)
Search: O(log n)
Insert: O(log n)
Delete: O(log n)
    For most trees, this is true even in the worst case
    For binary search trees, in the worst case these are O(n)
    This is because binary search trees are not guarenteed to be balanced
        The worse case height of a tree with n nodes in n-1
        Therefore our operations could be O(n)
        5
       4
      3
     2
    1

Space: O(n)
"""

# Binary Search Tree Implementation, iterative methods
class BST:

    def __init__(self):
        self.root = None

    def insert(self, node):
        curr = self.root
        prev = None
        while curr is not None:
            prev = curr
            if node.data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        if prev is None:
            self.root = node
        elif node.data < prev.data:
            prev.left = node
        else:
            prev.right = node
            
    def remove(self, node):
        if self.search(node.data) is False:
            return False
        
        prev = None
        curr = self.root
        while curr is not None and curr.data != node.data:
            prev = curr
            if curr.data < node.data:
                curr = curr.right
            else:
                curr = curr.left
        
        if curr.left is None or curr.right is None:
            newCurr = None
            if curr.left is None:
                newCurr = curr.right
            else:
                newCurr = curr.left
            if prev == None:
                return
            if curr == prev.left:
                prev.left = newCurr
            else:
                prev.right = newCurr
            curr = None

        else:
            p = None
            temp = curr.right
            while temp.left is not None:
                p = temp
                temp = temp.left
            if p is not None:
                p.left = temp.right
            else:
                curr.right = temp.right
            curr.data = temp.data
            temp = None
        return

    def search(self, data):
        searchNode = self.root
        while searchNode:
            if searchNode.data == data:
                return True
            elif data < searchNode.data:
                searchNode = searchNode.left
            else:
                searchNode = searchNode.right
        return False
            
    def preOrder(self, node):
        if node is None:
            return
        print(node.data)
        self.preOrder(node.left)
        self.preOrder(node.right)

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(5)
    node4 = Node(10)
    node5 = Node(0)
    node6 = Node(4)
    bst = BST()
    bst.insert(node1)
    bst.insert(node2)
    bst.insert(node3)
    bst.insert(node4)
    bst.insert(node5)
    bst.insert(node6)
    bst.preOrder(bst.root)
    print(bst.search(1))
    print(bst.search(2))
    print(bst.search(5))
    print(bst.search(10))
    print(bst.search(0))
    print(bst.search(4))
    print(bst.search(-2))
    print(bst.search(3))
    print(bst.search(100))
    bst.remove(node3)
    print(bst.search(5))
    bst.preOrder(bst.root)
    bst.insert(Node(6))
    bst.insert(Node(5))
    print('added 5 back in and 6')
    bst.preOrder(bst.root)
    print('remove the root')
    bst.remove(node1)
    bst.preOrder(bst.root)
    print('remove the root again, and add more nodes')
    bst.remove(node2)
    bst.insert(Node(50))
    bst.insert(Node(25))
    bst.insert(Node(33))
    bst.insert(Node(1))
    bst.insert(Node(7))
    bst.insert(Node(3))
    bst.preOrder(bst.root)
    
if __name__ == "__main__":
    main()