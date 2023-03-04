def countingsort(array, zeroarray, k):
    countingArray = [0] * (k+1)
    print("Generating counting array: ")
    for j in range(len(array)):
        countingArray[array[j]] += 1
        print(countingArray)
    print("\nCreating accumulated sum on counting array: ")
    for i in range(1, k+1):
        countingArray[i] += countingArray[i-1]
        print(countingArray)
    print("\nCreating sorted array: ")
    for j in range(len(array) - 1, -1, -1):
        zeroarray[countingArray[array[j]] - 1] = array[j]
        countingArray[array[j]] -= 1
        print(zeroarray)

array1 = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
zeroarray1 = [0] * len(array1)
k = max(array1)
countingsort(array1, zeroarray1, k)