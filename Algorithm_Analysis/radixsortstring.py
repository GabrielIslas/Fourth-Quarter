import math

def insert_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

def letter(string, index):
    if len(string) < index + 1:
        return 0
    else:
        return string[len(string) - 1 - index]


def bucketsort(array, exponent):
    buckets = [[] for _ in range (ord("Z") - ord("A") + 1)]
    for string in array:
        buckets[ord(letter(string, exponent))-ord("A")].append(string)
    for i in range(10):
        insert_sort(buckets[i])
    resultArray = []
    for bucket in buckets:
        resultArray.extend(bucket)
    print(f"Buckets: {buckets}")
    print(f"Resulting array: {resultArray}")
    return resultArray
    

def radixsort(array):
    arrayInUse = array
    digitIndex = 3
    for i in range(digitIndex):
        arrayInUse = bucketsort(arrayInUse, i)



arr3 = ["COW", "DOG", "SEA", "RUG", "ROW", "MOB", "BOX", "TAB", "BAR", "EAR", "TAR", "DIG", "BIG", "TEA", "NOW", "FOX"]
radixsort(arr3)