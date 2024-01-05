# Purpose: Code and explain what Merge Sort is

# What is Merge Sort?
"""
Merge sort is a sorting algorithm that works by dividing the array into smaller subarrays,
    sorting each subarray, and then merging the sorted subarrays back together to form
    the final sorted array
"""

# Big O
"""
Time Complexity: O(n log(n))
Space Complexity: O(n)
"""

# Merge Sort implementation (https://www.programiz.com/dsa/merge-sort)
def mergeSort(arr):
    if len(arr) > 1:
        
        right = len(arr) // 2
        left = arr[:right]
        mid = arr[right:]

        mergeSort(left)
        mergeSort(mid)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(mid):
            if left[i] < mid[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = mid[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(mid):
            arr[k] = mid[j]
            j += 1
            k += 1

def main():
    arr = [10, 9, 4, 3, 5, 77, 12]
    print('Array before sort: ', arr)
    mergeSort(arr)
    print('Array after merge sort: ', arr)

if __name__ == "__main__":
    main()