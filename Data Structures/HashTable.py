# Purpose: Learn and provide examples of a Hash Table

# What is a Hash Table?
"""
Data structure that represents a dynamic set of data
Can be implemented in multiple ways, but usually is a combination of two things:
    A hash function, which returns a non-negative integer known as the hash code
    An array capable of storing data of the type we wish to place into the hash 
    table
    We run our data through the hash function, and store that data in the 
    element of the array returned by the hash code

Example:

Hash Table (hash_code, data)

0 data
1 data
2 data
3 data
4 data

hash_code = hash("Corey")
// let's say hash_code = 3
hashtable[hash_code] = "Corey"

0
1
2
3 "Corey"
4
"""

# What is a Hash Table useful for?
"""
Great at quick searches/inserts/deletions, but bad at ordering or sorting data
Useful for tons of problems such as:
    Finding duplicates
    Detecting anagrams
    Searching for substrings
    Database
    Caching
    Compression
"""

# Hash Functions
"""
Hash functions are what gives us our hash code, which in turn tells us where to 
store the data in the array
There's tons of different hash functions, some good and some bad
A good hash function should:
    Use only the data being hashed
    Use all of the data being hashed
    Be deterministic
        hash("corey") == hash("corey"), every time
    Uniformly distirbute the data
    Generate different hash codes for very similar data
"""

# Collisions and Linear Probing
"""
A collision is when a hash function returns the same hash code for two pieces of
different data
    hash("corey") == 4
    hash("corei") == 4
One technique to resolve this is called "Linear Probing"
    If we have a collision, we try to place the data in the next consecutive 
    element in the array
    We wrap around the beginning if necessary, until we find a vacancy
    However, this can cause clustering. Once there is a miss, two adjacent cells
    will contain data, making the cluster more likely to grow
    Additionally, we only can store as much data as we have locations for in our 
    array
"""

# Chaining
"""
Chaining is a better way to solve collisions
Instead of each element of the array holding just one peice of data, it holds 
multiple
Each element of the array could be a pointer to head of a linked list
    That way multiple pieces of data can yield the same hash code and we can 
    still store it all
This resolves collisions and clustering problems
"""

# Hash Table operations and space
"""
Access: NA
Search: O(1)
Insert: O(1)
Delete: O(1)
    Note that these can be O(n) in the worst case
    For example, if we have a bad hash function

Space: O(n)
"""

# Hash Table via Dictionary
hTable = {'a': 1, 'b' : 2, 'c': 3}
hTable.update({'d' : 4})
print(hTable)
print(hTable.get('d'))
print(hTable.keys())
print(hTable.values())
print(hTable.items())
print(hTable.pop('a'))

# Custom Hash Table, int keys only
# Does not support collisions, so keys could overwrite each other!
class myHTable:

    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hash(self, key):
        # A very basic hash function
        hash_code = (int(key) % self.size)
        return hash_code

    def add(self, key, value):
        idx = self.hash(key)
        self.table[idx] = [key, value]

    def exists(self, key):
        lookUp = self.table[self.hash(key)]
        if lookUp and lookUp[0] == key:
            return True
        return False

    def get(self, key):
        if self.exists(key):
            return self.table[self.hash(key)]
        return False

    def remove(self, key):
        if self.exists(key):
            self.table[self.hash(key)] = None
            return True
        return False

def main():
    ht = myHTable(50)
    ht.add(5, '500')
    ht.add(200, 'hello')
    ht.add(201, 'world')
    print(ht.table)
    print(ht.exists(5))
    print(ht.exists(300))
    print(ht.get(5))
    print(ht.get(300))
    ht.remove(5)
    ht.remove(300)
    print(ht.exists(5))

if __name__ == "__main__":
    main()