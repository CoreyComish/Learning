# Purpose: Learn and provide examples of Big O

# What is Big O?
"""
Big O is a mathematical notation
It is used to describe the upper bound time complexity of algorithms
It can also describe the upper bound space complexity of a data structure
Upper bound == Worst Case
"""

# What is log?
"""
Logarithm or log is the inverse function to exponentiation
The power (exponent) to which one base number must be mutliplied by itself to produce another number
    log(100) = 2, because 10^2 = 100
    log(1000) = 3, 10^3 = 1000
    The above assumes that base is = 10
    log(4)
        if base=2, then log(4) = 2
        if base=10, then log(4) = 0.60206
    Generally in Computer Science, base is assumed to be 2
    2^? = 8 --> Log2(8) = 3
When discussing Big O, the log base is irrelevant
    This is because every base can be converted with multiplication by a constant
    In Big O notation, constant factors are removed
"""

# Why does this matter?
"""
It shows how run time or space requirements grow as the input size grows
Useful for determining how efficient an algorithm or data structure might be, espically as size grows
"""

# O(1) Algorithm - (Indexing array) - Constant Time
def constAlgo(arr):
    if len(arr) == 0: # O(1) operation
        return None
    return arr[0] # O(1) operation
"""
Why is this O(1)?
    Both operations are constant time, it doesnt matter the size of arr
        If len(arr) meant we had to traverse every element in arr and increase count by 1,
        then len(arr) would be O(n)
"""

# O(log n) Algorithm - (Binary Search) - Logarithmic Time
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
            return str(mid) + " True"
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

# O(n) Algorithm - Traverse 1D Array - Linear Time
def traverse1D(arr1D):
    for ele in arr1D:
        print(ele)
"""
Why is this O(n)?
    We iterate once through n elements, printing each one
"""

# O(n log n) Algorithm - Quasilinear Time
def searchBinarySearch(arr, x):
    for li in arr:
        print(binarySearch(li, x))
"""
Why is this O(n log n)?
    We iterate through each element in li = n
    For each of those elements, we use binary search which = log n
    Therefore, O(n log n)

    This is a quick and easy way to demonstrate this time complexity
    A more advanced O(n log n) algorithm is merge sort
"""

# O(n^2) Algorithm - Traverse 2D Array - Quadratic Time
def traverse2D(arr2D):
    for ele in arr2D:
        for num in ele:
            print(num)
"""
Why is this O(n^2)?
    We iterate through n elements
    Within each element we iterate through n numbers
    = n * n = n^2
"""

# O(2^n) Algorithm - Exponential Time
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""
Why is this O(2^n)?
    Lets say that we give this algorithm n=4
    The recursion tree will look something like this:

                    4
                3       2
              2  1     1 0
             1 0

    Notice how the depth of the tree = 3
    In reality, the complexity of this is O(2^n-1)
    But since we get rid of constants, it becomes O(2^n)
    Each level grows exponentially, level 3 = 2^3, level 2 = 2^2
"""

# O(n!) Algorithm - Factorial Time
def factorial(n):
    if n == 0:
        print("***********")
    for i in range(0, n):
        factorial(n-1)
"""
Why is this O(n!)?
    Lets say n = 4
    This would print out 24 star lines, using recursion
    4! = 4 * 3 * 2 * 1 = 24
    If we plotted the recursive calls out in tree form, there would be 24 times where factorial(0)
"""

def main():
    print(constAlgo([1,2,3]))
    print(binarySearch([1,2,3,4,5,6,7], 7))
    traverse1D([1,2,3])
    searchBinarySearch([[1,2,3], [3, 4, 5], [5, 6, 10]], 3)
    traverse2D([[1,1], [2,2], [3,3], [4,4]])
    print(fibonacci(4))
    factorial(4)

if __name__== "__main__": 
    main() 