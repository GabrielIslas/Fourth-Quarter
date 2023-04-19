# Dynamic programming
# Step 1. Define objective function
# Step 2. Define base case
# Step 3. Define recurrence

import math

def change_make(change, coins):
    F = [0]
    coinsChange = [0]
    for i in range(1, change+1):
        temp = math.inf
        j = 0
        finalCoin = -1
        while j < len(coins) and i >= coins[j]:
            if(F[i - coins[j]] < temp):
                finalCoin = coins[j]
                temp = F[i - coins[j]]
            j += 1
        coinsChange.append(finalCoin)
        F.append(temp+1)
    coinsUsed = []
    temp = change
    while coinsChange[temp] != 0:
         coinsUsed.append(coinsChange[temp])
         temp -= coinsChange[temp]
    return (F[change], coinsUsed)


coin_types = [1, 3, 5, 8, 14, 25]
changegoal = 74
print(change_make(changegoal, coin_types))

