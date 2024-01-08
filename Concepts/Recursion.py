# Purpose: Take a look at recursion, what it means, and what it is

# What is recursion?
"""
Recursion is simply a function that calls itself from within

Recursive functions contain at least one base case
    The base case is the problem that we know the answer to,
    and it can be solved without any more recursive calls.
    
    The base case stops the recursion from continuing on forever
"""

# Why is recursion useful?
"""
Helps break down the problem into smaller ones
Sometimes provides a simpler more elegant solution
"""

# Where is recursion used?
"""
Fibonacci, Factorial, Depth First Search Traversal
"""

# What are the downsides to recursion?
"""
It creates substantial overhead
    Each time the function calls itself space must be allocated
    and a copy of the variables/parameters is created
"""

# Example
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    print(fibonacci(10))

if __name__ == "__main__":
    main()