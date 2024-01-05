# Purpose: Code and explain what Quick Sort is

# What is Quick Sort?
"""
Quick sort is a sorting algorithm that picks an element as a pivot and partitions the
    given array around the picked pivot by placing the pivot in its correct position
    in the sorted array
"""

# Big O
"""
Time Complexity: O(n^2)
Space Complexity: O(log(n))
"""

# Quick Sort implementation (https://www.programiz.com/dsa/quick-sort)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)

def main():
    arr = [10, 9, 4, 3, 5, 77, 12]
    print('Array before sort: ', arr)
    quickSort(arr, 0, len(arr)-1)
    print('Array after quick sort: ', arr)

if __name__ == "__main__":
    main()