# Purpose: Code and explain Depth First Search (DFS)

# What is DFS?
"""
Depth first search is a searching algorithm used on graphs or trees
DFS searches vertically before horizontally
A Stack is used for implementing this algorithm

General Steps:
    1. Add starting root Node to the Stack
    2. Pop the Node from the stack
    3. Insert the Node's children into the stack
    4. Mark the popped Node as visited / compare to the search
    Repeat Steps 2-4
"""

# Why is DFS useful?
"""
Some examples of useful applications:
    Scheduling problems
    Cycle detection in graphs
    Solving a maze or sudoku puzzle
    Topological sorting
    Decision Tree
"""

# DFS Big O?
"""
Trees:
    Run Time:
        O(n)
        In the worst case, we touch every node

    Space Complexity:
        O(n)
        In the worst case, we are holding all the nodes in our Stack

Graphs:
    Run Time:
        O(V + E)
        In the worst case, we iterate through every edge and vertice

    Space Complexity:
        O(V)
        In the worst case, we hold all the vertices in our Stack
"""

# DFS implementation, using BST
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

    def DFS(self, data):
        if self.root is None:
            return False
        stack = [self.root]
        while len(stack) > 0:
            visited = stack.pop()
            if visited.data == data:
                return True
            if visited.left:
                stack.append(visited.left)
            if visited.right:
                stack.append(visited.right)
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
    bst = BST()
    bst.insert(Node(5))
    bst.insert(Node(2))
    bst.insert(Node(1))
    bst.insert(Node(100))
    bst.insert(Node(25))
    print(bst.DFS(5))
    print(bst.DFS(2))
    print(bst.DFS(1))
    print(bst.DFS(100))
    print(bst.DFS(25))
    print(bst.DFS(33))
    print(bst.DFS(4))

if __name__ == "__main__":
    main()