# Purpose: Learn and provide examples of Big O

# What is Big O?
"""
- Big O is a mathematical notation
- It is used to describe the upper bound time complexity of algorithms
- It can also describe the upper bound space complexity of a data structure
- Upper bound == Worst Case
"""

# What is log?
"""
- Logarithm or log is the inverse function to exponentiation
- The power (exponent) to which one base number must be mutliplied by itself to produce another number
    -log(100) = 2, because 10^2 = 100
    -log(1000) = 3, 10^3 = 1000
    -The above assumes that base is = 10
    -log(4)
        -if base=2, then log(4) = 2
        -if base=10, then log(4) = 0.60206
    -Generally in Computer Science, base is assumed to be 2
    - 2^? = 8 --> Log2(8) = 3
- When discussing Big O, the log base is irrelevant
    - This is because every base can be converted with multiplication by a constant
    - In Big O notation, constant factors are removed
"""

# Why does this matter?
"""
- It shows how run time or space requirements grow as the input size grows
- Useful for determining how efficient an algorithm or data structure might be, espically as size grows
"""

# O(1) Algorithm - (Indexing array)
def constAlgo(arr):
    if len(arr) == 0: # O(1) operation
        return None
    return arr[0] # O(1) operation

# O(log n) Algorithm - (Binary Search)
def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return False
"""
Why is this O(log n)?
    n = 8
    [0, 1, 2, 3, 4, 5, 6, 7]
    we search for 7
    [4, 5, 6, 7], 1st operation
    [6, 7], 2nd operation
    [7], 3rd operation
    log(n) = log(8) = 3
"""

# TODO: Implement O(n log n) Algorithm

# TODO: Implement O(n^2) Algorithm

# TODO: Implement O(2^n) Algorithm

# TODO: Implement O(n!) Algorithm

def main():
    print(constAlgo([1,2,3]))
    print(binarySearch([1,2,3,4,5,6,7], 7))

if __name__=="__main__": 
    main() 