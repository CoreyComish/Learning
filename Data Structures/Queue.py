# Purpose: Learn and provide examples of a Queue

from collections import deque

# What is a Queue?
"""
Data structure that represents a dynamic set of data
First In, First Out /// Last In, Last Out
Think of it as a physical line of people at a movie theater door
Inserting or Enqueue puts at the end of the queue
Deleting or Dequeue removes from the front of the queue

Often implemented via doubly linked list
"""

# What is a Queue useful for?
"""
CPU and Disk Schedule
Spotify - music queue
Breadth first search
MMO login system with full servers
"""

# Queue operations and size
"""
Access: O(n)
Search: O(n)
Insert: O(1), since we can only add to the end
Delete: O(1), since we can only remove from the front

Space: O(n)
"""

# Queue implementation, using collections Dequeue
class Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.popleft()
    
# Queue implementation, using doubly linked list
class QueueD:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            node.prev.next = node
            self.tail = node

    def dequeue(self):
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

    def walk(self):
        queueItems = []
        currItem = self.head
        while currItem is not None:
            queueItems.append(currItem.data)
            currItem = currItem.next
        return queueItems
    
    def reverseWalk(self):
        queueItems = []
        currItem = self.tail
        while currItem is not None:
            queueItems.append(currItem.data)
            currItem = currItem.prev
        return queueItems

class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def main():
    myQueue = Queue()
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    print(myQueue.queue)
    myQueue.dequeue()
    print(myQueue.queue)
    myQueue.dequeue()
    print(myQueue.queue)
    myQueue.dequeue()
    print(myQueue.queue)

    myQueueD = QueueD()
    node1 = Node(5)
    node2 = Node(10)
    node3 = Node(15)
    node4 = Node(20)
    myQueueD.enqueue(node1)
    myQueueD.enqueue(node2)
    myQueueD.enqueue(node3)
    print(myQueueD.walk())
    #print(str(myQueueD.reverseWalk()) + ' Reverse Order')
    myQueueD.dequeue()
    print(myQueueD.walk())
    #print(str(myQueueD.reverseWalk()) + ' Reverse Order')
    myQueueD.dequeue()
    print(myQueueD.walk())
    #print(str(myQueueD.reverseWalk()) + ' Reverse Order')
    myQueueD.dequeue()
    print(myQueueD.walk())
    #print(str(myQueueD.reverseWalk()) + ' Reverse Order')

if __name__=="__main__": 
    main() 

