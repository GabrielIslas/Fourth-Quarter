import numpy as np

def lcs_length(X: str, Y: str):
    m, n = len(X), len(Y)
    b = np.zeros(shape = (m, n))
    c = np.zeros(shape = (m + 1, n + 1))
    for i in range(m + 1):
        c[i, 0] = 0
    for i in range(1, n + 1):
        c[0, i] = 0
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                b[i][j] = 3 # up left
            elif c[i][j+1] >= c[i+1][j]:
                c[i+1][j+1] = c[i][j+1]
                b[i][j] = 2 # up
            else:
                c[i+1][j+1] = c[i+1][j]
                b[i][j] = 1 # left
    return (c, b)

def print_lcs(b: np.ndarray, X: str, i: int, j: int):
    if i == -1 or j == -1:
        return
    if b[i][j] == 3:
        print_lcs(b, X, i-1, j-1)
        print(X[i])
    elif b[i][j] == 2:
        print_lcs(b, X, i-1, j)
    else:
        print_lcs(b, X, i, j-1)

x = "abcbdabaabb"
y = "bdcabaaababb"
results = lcs_length(x, y)

print(results[0])
print(results[1])
print_lcs(results[1], x, len(x)-1, len(y)-1)


