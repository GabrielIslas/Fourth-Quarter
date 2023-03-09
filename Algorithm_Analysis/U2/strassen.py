import numpy as np

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

        P1 = strassen(A11, S1)
        P2 = strassen(S2, B22)
        P3 = strassen(S3, B11)
        P4 = strassen(A22, S4)
        P5 = strassen(S5, S6)
        P6 = strassen(S7, S8)
        P7 = strassen(S9, S10)

        C[:n//2, :n//2] = P5 + P4 - P2 + P6
        C[:n//2, n//2:] = P1 + P2
        C[n//2:, :n//2] = P3 + P4
        C[n//2:, n//2:] = P5 + P1 - P3 - P7
    
    return C