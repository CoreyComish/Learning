# Purpose: Learn and provide examples of Linked Lists

# What is a Linked List?
"""
Data structure for storing objects in a linear order
Each object contains data and pointer to the next object
    If doubly linked, containes a pointer to the previous object
Can be used to implement other data structures - stacks, queues, hash tables
Head = start of linked list
Tail = end of linked list
"""

# What are the different types of Linked Lists?
"""
Singly linked list - data and pointer to next
Doubly linked list - data and pointers to prev and next
Circular linked list - data and pointer to next, tail points to head
Circular Doubly linked list - data and pointers to prev and next, tail points to head
"""

# Linked List opearations and size
"""
Access: O(n)
Search: O(n)
Insert: O(1)
    Beginning: O(1)
    End: O(1) if we keep track of tail, else O(n)
    Middle: O(1) but O(n) to find
Delete: O(1)
    Beginning: O(1)
    End: O(1) if we keep track of tail, else O(n)
    Middle: O(1) but O(n) to find

Space: O(n)

Compared to an array, it seems linked list is more efficent if we are doing
lots of inserts and deletions. An array is better if we need to do more accessing

LinkedList = Writes
Array = Reads
"""

# Linked List Implementation (Single)
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def search(self, target):
        node = self.head
        while node is not None:
            if node.data == target:
                return True
            else:
                node = node.next
        return False

    def delete(self, node):
        prev = self.head
        if prev is None:
            return False
        if prev is node:
            self.head = self.head.next
            return True
        else:
            while prev.next != node:
                prev = prev.next
                if prev is None:
                    return False
            prev.next = node.next
            return True
        
    def walk(self):
        currentNode = self.head
        nodeList = []
        while currentNode is not None:
            nodeList.append(currentNode.data)
            currentNode = currentNode.next
        return nodeList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def main():
    linkedList = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    # Insertions
    linkedList.insert(node1)
    print(linkedList.walk())
    linkedList.insert(node2)
    print(linkedList.walk())
    linkedList.insert(node3)
    print(linkedList.walk())
    linkedList.insert(node4)
    print(linkedList.walk())

    # Searches
    print(linkedList.search(1))
    print(linkedList.search(2))
    print(linkedList.search(3))
    print(linkedList.search(4))
    print(linkedList.search(5))

    # Delete
    print(linkedList.walk())
    linkedList.delete(node3)
    print(linkedList.walk())
    linkedList.delete(node1)
    print(linkedList.walk())
    linkedList.delete(node4)
    print(linkedList.walk())
    linkedList.delete(node2)
    print(linkedList.walk())

if __name__=="__main__": 
    main() 