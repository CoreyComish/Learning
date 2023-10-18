# Purpose: Learn and provide examples of Arrays/Lists

# What is an Array?
"""
A sequence of contiguous values, stored back to back to back
Could be all the same type [1, 2, 3]
Could be a mix of types ['hello', 5, 1.2, myObject]
Could be unsorted or sorted
"""

# Static Array
"""
A static array is an array in which the size is pre-defined and will not change
myStaticArr = [None] * 4 = [None, None, None, None]
    Technically this is still a dynamic array as we would be able to add/delete from it
    This is because all arrays/lists in Python are dynamic and resizable
    In C++ it would look something like:
        int scores[5] = {1, 5, 88, 32, 42};
"""
def staticArr():
    myStaticArr = [None] * 4
    for i in range(0, len(myStaticArr)):
        myStaticArr[i] = 'Static'
    print(myStaticArr)

# Dynamic Array
"""
A dynamic array is an array with automatic resizing
We can insert and delete elements from the array, and it resizes accordingly
"""
def dynamicArr():
    myDynamicArr = []
    for i in range(0, 6):
        myDynamicArr.append(i)
        print(myDynamicArr)

# Array Operations & Size
"""
Access: O(1)
Search: O(n)
Insert: O(n)
    Beginning: O(n)
    End: O(1)
    Middle: O(n)
Delete: O(n)
    Beginning: O(n)
    End: O(1)
    Middle: O(n)

Space: O(n)
"""
def arrOperations():
    sampleArr = [0,1,2,3,4]
    print("-------")
    print(sampleArr)
    print("-------")
    sampleArr.append(5)
    print('Appended 5: ' + str(sampleArr))
    sampleArr.pop()
    print('Popped: ' + str(sampleArr))
    sampleArr.insert(2, 10)
    print('Inserted 10 into idx 2: ' + str(sampleArr))
    print('Geting index 2: ' + str(sampleArr[2]))
    sampleArr[2] = 9
    print('Setting index 2: ' + str(sampleArr))
    sampleArr.remove(9)
    print('Removing element that = 9: ' + str(sampleArr))
    print('Length of arr: ' + str(len(sampleArr)))
    print('Min of arr: ' + str(min(sampleArr)))
    print('Max of arr: ' + str(max(sampleArr)))

# Algorithms invloving Array's
"""
The first one that comes to mind is binary search
Note that for this algorithm to work, the array must be SORTED
So lets use a sorting algorithm and then binary search it!
"""
def bubbleSort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def binarySearch(arr, ele):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < ele:
            low = mid + 1
        elif arr[mid] > ele:
            high = mid - 1
        else:
            return mid

    return -1

def main():
    staticArr()
    dynamicArr()
    arrOperations()
    print(bubbleSort([5,4,3,2,1]))
    print(binarySearch(bubbleSort([5,4,3,2,1]), 5))

if __name__=="__main__": 
    main() 