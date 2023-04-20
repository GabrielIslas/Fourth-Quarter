import numpy as np

def matrix_mult_bf(A: np.ndarray, B: np.ndarray):
    result = -1
    if A.shape[1] == B.shape[0]:
        result = np.zeros((A.shape[0], B.shape[1]))
        for i in range(A.shape[0]):
            for j in range(B.shape[1]):
                for k in range(B.shape[0]):
                    result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_mult_r(A: np.ndarray, B: np.ndarray):
    n = A.shape[0]
    C = np.zeros((n,n))
    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        A11 = A[:n//2, :n//2]
        A12 = A[:n//2, n//2:]
        A21 = A[n//2:, :n//2]
        A22 = A[n//2:, n//2:]

        B11 = B[:n//2, :n//2]
        B12 = B[:n//2, n//2:]
        B21 = B[n//2:, :n//2]
        B22 = B[n//2:, n//2:]

        C[:n//2, :n//2] = matrix_mult_r(A11, B11) + matrix_mult_r(A12, B21)
        C[:n//2, n//2:] = matrix_mult_r(A11, B12) + matrix_mult_r(A12, B22)
        C[n//2:, :n//2] = matrix_mult_r(A21, B11) + matrix_mult_r(A22, B21)
        C[n//2:, n//2:] = matrix_mult_r(A21, B12) + matrix_mult_r(A22, B22)
    return C 

# 7T(n/2) + Theta(n^2)
def strassen(A: np.ndarray, B: np.ndarray):
    n = A.shape[0]
    C = np.zeros((n,n))
    if n == 1:
        C = A * B
    else:
        A11 = A[:n//2, :n//2]
        A12 = A[:n//2, n//2:]
        A21 = A[n//2:, :n//2]
        A22 = A[n//2:, n//2:]

        B11 = B[:n//2, :n//2]
        B12 = B[:n//2, n//2:]
        B21 = B[n//2:, :n//2]
        B22 = B[n//2:, n//2:]

        S1 = B12 - B22
        S2 = A11 + A12
        S3 = A21 + A22
        S4 = B21 - B11
        S5 = A11 + A22
        S6 = B11 + B22
        S7 = A12 - A22
        S8 = B21 + B22
        S9 = A11 - A21
        S10 = B11 + B12
        print("S matrices")
        print(S1)
        print(S2)
        print(S3)
        print(S4)
        print(S5)
        print(S6)
        print(S7)
        print(S8)
        print(S9)
        print(S10)

        P1 = strassen(A11, S1)
        P2 = strassen(S2, B22)
        P3 = strassen(S3, B11)
        P4 = strassen(A22, S4)
        P5 = strassen(S5, S6)
        P6 = strassen(S7, S8)
        P7 = strassen(S9, S10)
        print("P matrices")
        print(P1)
        print(P2)
        print(P3)
        print(P4)
        print(P5)
        print(P6)
        print(P7)

        C[:n//2, :n//2] = P5 + P4 - P2 + P6
        C[:n//2, n//2:] = P1 + P2
        C[n//2:, :n//2] = P3 + P4
        C[n//2:, n//2:] = P5 + P1 - P3 - P7
        print("C matrices")
        print(C[:n//2, :n//2])
        print(C[:n//2, n//2:])
        print(C[n//2:, :n//2])
        print(C[n//2:, n//2:])
    
    return C

matrixA = np.array([[1,0,2,1], [4,1,1,0], [0,1,3,0], [5,0,2,1]])
matrixB = np.array([[0,1,0,1], [2,1,0,4], [2,0,1,1], [1,3,5,0]])
print(strassen(matrixA, matrixB))