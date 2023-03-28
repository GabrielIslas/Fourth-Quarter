import numpy as np

def min_sum_triangle(triangle: list):
    sumStorage = np.empty(len(triangle))
    triangleRows = len(triangle) - 1
    minStorage = np.empty(len(triangle))

    for i in range(len(triangle[triangleRows])):
        sumStorage[i] = triangle[triangleRows][i]
    
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            sumStorage[j] = triangle[i][j] + min(sumStorage[j], sumStorage[j+1])
            minStorage[j] = min(sumStorage[j], sumStorage[j+1])
        print(minStorage)
        

    

    return sumStorage[0]


triangle1 = [[2],
             [3,9],
             [1,6,7]]

triangle2 = [[2],[5,4],[1,4,7],[8,6,9,6]]

print(min_sum_triangle(triangle2))



