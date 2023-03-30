# solve with dynamic programming
def knapSack(capacity, weights, values):
    n = len(values)
    # Making the dp array
    dp = [0 for i in range(capacity+1)]
 
    # Taking first i elements
    for i in range(1, n+1):
       
        # Starting from back,
        # so that we also have data of
        # previous computation when taking i-1 items
        for w in range(capacity, 0, -1):
            if weights[i-1] <= w:
                 
                # Finding the maximum values
                dp[w] = max(dp[w], dp[w-weights[i-1]]+values[i-1])
     
    # Returning the maximum value of knapsack
    return dp[capacity]
 
 
