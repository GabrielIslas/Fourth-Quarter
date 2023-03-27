import numpy as np
import matplotlib.pyplot as plt
import time
import random

def matrix_mult_bf(A: np.ndarray, B: np.ndarray):
    result = -1
    if A.shape[1] == B.shape[0]:
        result = np.zeros((A.shape[0], B.shape[1]))
        for i in range(A.shape[0]):
            for j in range(B.shape[1]):
                for k in range(B.shape[0]):
                    result[i][j] += A[i][k] * B[k][j]
    return result

def strassen(A: np.ndarray, B: np.ndarray, limit: int):
    n = A.shape[0]
    C = np.zeros((n,n))
    if n <= limit:
        C = matrix_mult_bf(A, B)
    else:
        P1 = strassen(A[:n//2, :n//2], B[:n//2, n//2:] - B[n//2:, n//2:], limit)
        P2 = strassen(A[:n//2, :n//2] + A[:n//2, n//2:], B[n//2:, n//2:], limit)
        P3 = strassen(A[n//2:, :n//2] + A[n//2:, n//2:], B[:n//2, :n//2], limit)
        P4 = strassen(A[n//2:, n//2:], B[n//2:, :n//2] - B[:n//2, :n//2], limit)
        P5 = strassen(A[:n//2, :n//2] + A[n//2:, n//2:], B[:n//2, :n//2] + B[n//2:, n//2:], limit)
        P6 = strassen(A[:n//2, n//2:] - A[n//2:, n//2:], B[n//2:, :n//2] + B[n//2:, n//2:], limit)
        P7 = strassen(A[:n//2, :n//2] - A[n//2:, :n//2], B[:n//2, :n//2] + B[:n//2, n//2:], limit)

        C[:n//2, :n//2] = P5 + P4 - P2 + P6
        C[:n//2, n//2:] = P1 + P2
        C[n//2:, :n//2] = P3 + P4
        C[n//2:, n//2:] = P5 + P1 - P3 - P7
    
    return C

# Define matrix sizes to test
matrix_sizes = [2**i for i in range(1,10)]

# Measure runtime for each matrix size
times_strassen1 = []
times_strassen2 = []
times_strassen4 = []
times_strassen8 = []
times_strassen16 = []
times_strassen32 = []
times_strassen64 = []

for size in matrix_sizes:
    A = np.random.randint(0, 100, (size, size))
    B = np.random.randint(0, 100, (size, size))
    
    start_time_st = time.time()
    print(strassen(A, B, 1))
    times_strassen1.append(time.time() - start_time_st)

    start_time_st = time.time()
    print(strassen(A, B, 2))
    times_strassen2.append(time.time() - start_time_st)
    
    start_time_st = time.time()
    print(strassen(A, B, 4))
    times_strassen4.append(time.time() - start_time_st)
    
    start_time_st = time.time()
    print(strassen(A, B, 8))
    times_strassen8.append(time.time() - start_time_st)
    
    start_time_st = time.time()
    print(strassen(A, B, 16))
    times_strassen16.append(time.time() - start_time_st)
    
    start_time_st = time.time()
    print(strassen(A, B, 32))
    times_strassen32.append(time.time() - start_time_st)
    
    start_time_st = time.time()
    print(strassen(A, B, 64))
    times_strassen64.append(time.time() - start_time_st)
    
print(matrix_sizes)



plt.figure(figsize=(20, 16))

# Plot runtimes
plt.plot(matrix_sizes, times_strassen1, label='1')
plt.plot(matrix_sizes, times_strassen2, label='2')
plt.plot(matrix_sizes, times_strassen4, label='4')
plt.plot(matrix_sizes, times_strassen8, label='8')
plt.plot(matrix_sizes, times_strassen16, label='16')
plt.plot(matrix_sizes, times_strassen32, label='32')
plt.plot(matrix_sizes, times_strassen32, label='64')
plt.legend()
plt.show()