# Purpose: Code and explain what a Heap is

# What is a Heap?
"""
A heap is a specalized tree-based data structure
A heap satisfies the 'heap property'
    The heap property could be min-heap or max-heap
In a max-heap, the parent node is always greater than it's children
In a min-heap, the parent node is always less than it's children
Heaps are usually implemented via a priority queue
In the priority queue, the max/min will always be stored at the 0th idx of the array
"""

# Why is it useful?
"""
Heaps are useful for when the highest or lowest order/priority element needs to
    be accessed or removed, since it can be done in O(1) time
Priority Queue's (MMO login system, oldest accounts get in first?)
Selection Algorithms
Quickly finding min or max
"""

# Heap Big O?
"""
Big O varies depending on the heap's properties
Access: O(1) - Assuming implemented via priority queue
Search: O(n)
Insert: O(log n)
Delete: O(log n)

Space: O(n)
"""

# Heap implementation
import heapq
def main():
    arr = [5, 4, 20, 1, 10, 7]
    heapq.heapify(arr)
    print(list(arr))
    heapq.heappush(arr, 0)
    print(list(arr))
    heapq.heappop(arr)
    print(list(arr))
    print(heapq.nlargest(3, arr)) # 3 largest numbers
    print(heapq.nsmallest(3, arr)) # 3 smallest numbers

if __name__ == "__main__":
    main()