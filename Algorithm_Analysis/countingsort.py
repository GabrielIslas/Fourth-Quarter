def countingsort(array, zeroarray, k):
    countingArray = [0] * (k+1)
    for j in range(len(array)):
        countingArray[array[j]] += 1
    for i in range(1, k+1):
        countingArray[i] += countingArray[i-1]
    for j in range(len(array) - 1, -1, -1):
        zeroarray[countingArray[j]] 

array1 = [2,5,3,0,2,3,0,3]
zeroarray1 = [0] * len(array1)
k = max(array1)