def bubble_sort(array):
    indicator = True
    for _ in range(len(array) - 1):
        if indicator is False:
            break
        print(array)
        indicator = False
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                indicator = True
       

arr1 = [7, 3, 9, 4, 2, 5, 6, 1, 8]
arr2 = [3, 5, 2, 9, 8, 1, 6, 4, 7]
bubble_sort(arr2)

