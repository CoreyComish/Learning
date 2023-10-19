# Purpose: Learn and provide examples of a Stack

# What is a Stack?
"""
Data structure that represents a dynamic state of data
First In, Last Out /// Last In, First Out
Think of it as a physical stack of items
Pushing adds to the stack, popping removes the item on top of the stack
"""

# What is a Stack useful for?
"""
Useful for lots of different algorithms!
Backtracking
    Finding correct path through a maze
Compile time memory management
    Recursive functions
Depth First search
Undo & Redo
"""

# Stack operations and size
"""
Access: O(n)
Search: O(n)
Insert: O(1), since we can only add to the top
Delete: O(1), since we can only pop from the top

Space: O(n)
"""

# Stack implementation
class Stack:
    
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        # Trivial implementation, just showing what happens (could use built-in pop)
        popped = self.stack[-1]
        self.stack = self.stack[0:-1]
        return popped

def main():
    myStack = Stack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    print(myStack.stack)
    myStack.pop()
    print(myStack.stack)

if __name__=="__main__": 
    main() 