def partition(array, startIndex, finalIndex):
    x = array[finalIndex]
    i = startIndex - 1
    for j in range(startIndex, finalIndex):
        if array[j] <= x:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[finalIndex] = array[finalIndex], array[i+1]
    return i + 1

def quicksort(array, startIndex, finalIndex):
    print("Start: " + str(array[startIndex]) + " End: " + str(array[finalIndex]), end = " ")
    if startIndex < finalIndex:
        q = partition(array, startIndex, finalIndex)
        print("Pivot: " + str(array[q]))
        quicksort(array, startIndex, q - 1)
        quicksort(array, q + 1, finalIndex)

array1 = [2, 8, 7, 1, 3, 5, 6, 4]
quicksort(array1, 0, 7)
print(array1)

