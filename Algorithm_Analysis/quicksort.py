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
    if startIndex < finalIndex:
        q = partition(array, startIndex, finalIndex)
        print(f"First: {array[startIndex]}, Last: {array[finalIndex]}, Pivot: {array[q]}")
        print("[", end = "")
        for i in range(startIndex, finalIndex + 1):
            print(f" {array[i]}", end = "")
        print(" ]")
        quicksort(array, startIndex, q - 1)
        quicksort(array, q + 1, finalIndex)
        
        

array1 = [23, 17, 21, 3, 42, 9, 13, 1, 2, 7, 35, 4]
array2 = [3, 9, 14, 12, 2, 17, 15, 8, 6, 18, 20, 1]
print("Operations on array 1")
print(array1)
quicksort(array1, 0, 11)
print(array1)

print("Operations on array 2")
print(array2)
quicksort(array2, 0, 11)
print(array2)

