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
    print(array)
    HeapBuild(array)
    print(f"Heap: {array}")
    print("HeapSort steps: ")
    heapSize = len(array)
    for _ in range(heapSize - 1):
        array[0], array[heapSize - 1] = array[heapSize - 1], array[0]
        heapSize -= 1
        Heapify(array, heapSize, 0)
        print(array)


array1 = [23, 17, 21, 3, 42, 9, 13, 1, 2, 7, 35, 4]
HeapSort(array1)

