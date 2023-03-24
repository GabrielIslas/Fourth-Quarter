import numpy as np
import math

def maxsubarray_bf(A: list):
    if len(A) == 0:
        return 0
    
    maxSum = A[0]
    for i in range(len(A)):
        currentSum = 0
        for j in range(i, len(A)):
            currentSum += A[j]
            maxSum = max(maxSum, currentSum)
    return maxSum

def maxsubarray_dc(A: list, left=None, right=None):
    if len(A) == 0:
        return 0
    if left is None and right is None:
        left, right = 0, len(A) - 1
    if right == left:
        return A[left]
    middle = (left + right) // 2

    leftMax = -math.inf
    total = 0
    for i in range(middle, left - 1, -1):
        total += A[i]
        if total > leftMax:
            leftMax = total
    
    rightMax = -math.inf
    total = 0
    for i in range(middle + 1, right + 1):
        total += A[i]
        if total > rightMax:
            rightMax = total

    maxLeftRight = max(maxsubarray_dc(A, left, middle), maxsubarray_dc(A, middle + 1, right))

    return max(maxLeftRight, leftMax + rightMax)



numbers = [-2,1,-3,4,-1,2,1,-5,4]

print(maxsubarray_dc(numbers))
    
