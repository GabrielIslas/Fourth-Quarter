import math
def shellsort(array, gaps):
    counter = 0
    print(array)
    size = len(array)
    for gap in gaps:
        for i in range(gap, size):
            temp = array[i]
            j = i
            counter += 1
            while j >= gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                j -= gap
            array[j] = temp
            print(array)
    print("Total Comparisons: " + str(counter))
        

gaps1 = [5, 2, 1]
arr1 = [7, 3, 9, 4, 2, 5, 6, 1, 8]
arr2 = [3, 5, 2, 9, 8, 1, 6, 4, 7]
shellsort(arr2, gaps1)

