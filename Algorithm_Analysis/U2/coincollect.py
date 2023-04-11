import numpy as np
import math

def coin_collecting(C: np.ndarray):
    n, m = C.shape
    F = np.zeros(shape = (n, m))
    F[0][0] = C[0][0]
    path = []
    for i in range(1, m):
        F[0][i] = F[0][i - 1] + C[0][i]
    for i in range(1, n):
        F[i][0] = F[i - 1][0] + C[i][0]
        for j in range(1, m):
            F[i][j] = max(F[i - 1][j], F[i][j - 1]) + C[i][j]
    # finding path
    indextemp = (n - 1, m - 1)
    while indextemp[0] != 0 and indextemp[1] != 0:
        if F[indextemp[0] - 1][indextemp[1]] >= F[indextemp[0]][indextemp[1] - 1]:
            path.append("down")
            indextemp = (indextemp[0] - 1, indextemp[1])
        else:
            path.append("right")
            indextemp = (indextemp[0], indextemp[1] - 1)
    for i in range(indextemp[0]):
        path.append("down")
    for i in range(indextemp[1]):
        path.append("right")
    path.reverse()
    return (F[n-1][m-1], path)

coinmap = np.random.randint(2, size = (5, 6))
coinmapwall = np.array([[0, -math.inf, 0, 1, 0, 0],
                         [1, 0, 0, -math.inf, 1, 0], 
                         [0, 1, 0, -math.inf, 1, 0], 
                         [0, 0, 0, 1, 0, 1], 
                         [-math.inf, -math.inf, -math.inf, 0, 1, 0]])
print(coinmapwall)
print(coin_collecting(coinmapwall))