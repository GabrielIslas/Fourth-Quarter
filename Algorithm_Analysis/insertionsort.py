def insert_sort(A):
    print(A)
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
        print(A)

arr1 = [7, 3, 9, 4, 2, 5, 6, 1, 8]
arr2 = [3, 5, 2, 9, 8, 1, 6, 4, 7]
insert_sort(arr1)
