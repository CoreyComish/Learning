# Purpose: Code and explain the binary search algorithm

# What is binary search?
"""
Binary search is a searching algorithm that finds the index of an element in a sorted array/list
It repeatedly divides the search in half
Think of looking for a particular page in a large book
    We are looking for page 125. We open the book in the middle to page 500.
        The page is higher than 125, so we take the left section and open in the middle
        We are now on page 250! Still to high, so we repeat
            There we go, we opened in the middle again and we are now on page 125
"""

# What is the Big O of binary search?
"""
Binary search runs in O(log n) with O(1) space
    O(log n) runtime because in the worst case the element we are searching for is at the start/end of the list
    [1,2,3,4,5,6,7,8]
        if we are searching for 1 it looks like
        n = 8
        [1,2,3,4,5,6,7,8] mid = 4
        [1,2,3] mid = 2
        [1] mid = 1 = found!
        3 operations
        log(n) = log(8) = 3
"""

# Binary Search
def binarySearch(arr, ele):
    high = len(arr) - 1
    low = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < ele:
            low = mid + 1
        elif arr[mid] > ele:
            high = mid -1
        else:
            return mid
    return -1

def main():
    for i in range(1, 7):
        print(binarySearch([1,2,3,4,5], i))

if __name__== "__main__": 
    main() 