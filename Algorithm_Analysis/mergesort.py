import math
import array

def merge_sort(array, startIndex, finalIndex):
    if startIndex < finalIndex:
        middle = math.floor((startIndex + finalIndex) / 2)
        merge_sort(array, startIndex, middle)
        merge_sort(array, middle + 1, finalIndex)
        merge(array, startIndex, middle, finalIndex)


def merge(array, startIndex, middle, finalIndex):
    n1 = middle - startIndex + 1
    n2 = finalIndex - middle

