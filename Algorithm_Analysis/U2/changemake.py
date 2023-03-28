# Dynamic programming
# Step 1. Define objective function
# Step 2. Define base case
# Step 3. Define recurrence

import math

coin_types = [2, 3, 5, 7, 11]
changegoal = 51

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
            temp = min(F[i - coins[j]], temp)
            j += 1
        coinsChange.append(finalCoin)
        F.append(temp+1)
    coinsUsed = []
    temp = change
    while coinsChange[temp] != 0:
         coinsUsed.append(coinsChange[temp])
         temp -= coinsChange[temp]
    return (F[change], coinsUsed)

print(change_make(changegoal, coin_types))

