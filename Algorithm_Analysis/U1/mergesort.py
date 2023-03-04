import math
import array

counter = 0

def merge_sort(array, startIndex, finalIndex):
    global counter
    if startIndex < finalIndex:
        middle = math.floor(startIndex + (finalIndex - startIndex) / 2)
        merge_sort(array, startIndex, middle)
        merge_sort(array, middle + 1, finalIndex)
        merge(array, startIndex, middle, finalIndex)
    """
    print("[", end = "")
    for i in range(startIndex, finalIndex + 1):
        print(f" {array[i]}", end = "")
    print(" ]")
    """
    
        
def merge(array, startIndex, middle, finalIndex):
    global counter
    n1 = middle - startIndex + 1
    n2 = finalIndex - middle
    leftList = [0] * (n1)
    rightList = [0] * (n2)
    for i in range(n1):
        leftList[i] = array[startIndex + i]
    for j in range(n2):
        rightList[j] = array[middle + j + 1]
    i = 0
    j = 0
    k = startIndex

    while i < n1 and j < n2:
        counter += 1
        if leftList[i] <= rightList[j]:
            array[k] = leftList[i]
            i += 1
        else:
            array[k] = rightList[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = leftList[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = rightList[j]
        j += 1
        k += 1


arr1 = [7, 3, 9, 4, 2, 5, 6, 1, 8]
arr2 = [3, 5, 2, 9, 8, 1, 6, 4, 7]
arr3 = [1, 2, 3, 4, 5, 6, 7, 8]
arr4 = [8, 7, 6, 5, 4, 3, 2, 1]
"""
print("Array 1")
merge_sort(arr1, 0, 8)
print("\nArray 2")
merge_sort(arr2, 0, 8)
"""
print("Comparisons array 3: ")
merge_sort(arr3, 0, 7)
print(counter)
counter = 0
print("Comparisons array 4: ")
merge_sort(arr4, 0, 7)
print(counter)
