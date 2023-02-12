import math

def insert_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

def digit(number, index):
    numberString = str(number)
    if len(numberString) < index + 1:
        return 0
    else:
        return int(numberString[len(numberString) - 1 - index])


def bucketsort(array, exponent):
    buckets = [[] for _ in range (10)]
    for number in array:
        buckets[digit(number, exponent)].append(number)
    for i in range(10):
        insert_sort(buckets[i])
    resultArray = []
    for bucket in buckets:
        resultArray.extend(bucket)
    print(resultArray)
    return resultArray
    

def radixsort(array):
    arrayInUse = array
    maxNumber = max(array)
    digitIndex = math.ceil(math.log10(maxNumber))
    for i in range(digitIndex):
        arrayInUse = bucketsort(arrayInUse, i)


arr1 = [1405, 975, 23, 9803, 4835, 2082, 7368, 573, 804, 746, 4703, 1421, 4273, 1208, 521, 2050]
arr2 = [117, 383, 4929, 144, 462, 1365, 9726, 241, 1498, 82, 1234, 8427, 237, 2349, 127, 462]
radixsort(arr2)
