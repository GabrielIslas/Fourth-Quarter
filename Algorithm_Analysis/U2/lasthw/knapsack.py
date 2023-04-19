# solve with dynamic programming
def knapSack(capacity, weights, values):
    n = len(values)
    dp = [0 for i in range(capacity+1)]
    for i in range(1, n+1):
        for w in range(capacity, 0, -1):
            if weights[i-1] <= w:
                dp[w] = max(dp[w], dp[w-weights[i-1]]+values[i-1])
    return dp[capacity]

def knapSack_dc(capacity, weights, values, size):
    if size == 0 or capacity == 0:
        return 0
    if weights[size-1] > capacity:
        return knapSack_dc(capacity, weights, values, size - 1)
    else:
        return max(values[size-1] + knapSack_dc(capacity - weights[size-1], weights, values, size-1), 
                   knapSack_dc(capacity, weights, values, size-1))
        
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
size = len(values)
print(knapSack_dc(capacity, weights, values, size))
print(knapSack(capacity, weights, values))
 
 
