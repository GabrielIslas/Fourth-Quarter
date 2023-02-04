def Heapify(array, heapSize, index):
    leftChild = 2 * index + 1
    rightChild = 2 * index + 2
    largest = index
    if leftChild < heapSize and array[leftChild] > array[largest]:
        largest = leftChild
    if rightChild < heapSize and array[rightChild] > array[largest]:
        largest = rightChild
    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        Heapify(array, heapSize, largest)


def HeapBuild(array):
    lastParent = len(array) // 2 - 1
    heapSize = len(array)
    for i in range(lastParent, -1, -1):
        Heapify(array, heapSize,  i)
    
def HeapSort(array):
    HeapBuild(array)
    heapSize = len(array)
    
    for _ in range(heapSize - 1):
        array[0], array[heapSize - 1] = array[heapSize - 1], array[0]
        heapSize -= 1
        Heapify(array, heapSize, 0)


array1 = [2, 9, 7, 6, 5, 8]
HeapSort(array1)
print(array1)
