import math
import array

def merge_sort(array, startIndex, finalIndex):
    if startIndex < finalIndex:
        middle = math.floor(startIndex + (finalIndex - startIndex) / 2)
        merge_sort(array, startIndex, middle)
        merge_sort(array, middle + 1, finalIndex)
        merge(array, startIndex, middle, finalIndex)


def merge(array, startIndex, middle, finalIndex):
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

merge_sort(arr1, 0, 8)
print(arr1)
