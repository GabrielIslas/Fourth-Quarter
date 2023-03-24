# Dynamic programming
# Step 1. Define objective function
# Step 2. Define base case
# Step 3. Define recurrence

import math

coin_types = [1,3,4]
changegoal = 32


def change_make(change, coins):
    F = [0]
    for i in range(1, change+1):
        temp = math.inf
        j = 0
        while j < len(coins) and i >= coins[j]:
            temp = min(F[i - coins[j]], temp)
            j += 1
        F.append(temp+1)
    print(F)
    return F[change]

print(change_make(changegoal, coin_types))

