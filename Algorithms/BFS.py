# Purpose: Code and explain what Breadth First Search (BFS) is

# What is BFS?
"""
Breadth First Search is a searching algorithm used on graphs or trees
Breadth means broad or wide, we search horizontally or level by level
BFS is implemented via a Queue

General Steps:
    1. Add Starting Root Node to Queue
    2. Extract the Node from the Queue
    3. Insert the extracted Node's children into the queue
    4. Mark the extracted Node as visited / Compare to Search
    Repeat 2-4
"""

# Why is BFS useful?
"""
Some examples of useful applications:
    Finding the shortest path in a graph
    Solving puzzles, like Rubiks Cubes
    Finding neighboring nodes in a Peer to Peer network
    Social Networking Website
"""

# BFS Big O?
"""
Trees:
    Run Time:
        O(n)
        In the worst case, we touch every node

    Space Complexity:
        O(n)
        In the worst case, we are holding all the nodes in our Queue

Graphs:
    Run Time:
        O(V + E)
        In the worst case, we iterate through every edge and vertice

    Space Complexity:
        O(V)
        In the worst case, we hold all the vertices in our Queue
"""

# BFS Implementation, using BST
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

    def BFS(self, data):
        if self.root is None:
            return False
        queue = [self.root]
        while len(queue) > 0:
            visited = queue.pop(0)
            if visited.data == data:
                return True
            if visited.left:
                queue.append(visited.left)
            if visited.right:
                queue.append(visited.right)
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
    print(bst.BFS(5))
    print(bst.BFS(2))
    print(bst.BFS(1))
    print(bst.BFS(100))
    print(bst.BFS(25))
    print(bst.BFS(33))
    print(bst.BFS(4))

if __name__ == "__main__":
    main()