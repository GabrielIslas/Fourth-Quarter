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

def greedy_change_make(change, coin_types):
    coinsUsed = 0
    coin_types.sort()
    while change > 0:
        for i in reversed(range(len(coin_types))):
            while coin_types[i] <= change:
                coinsUsed += 1
                change -= coin_types[i]
    return coinsUsed


coin_types = [1, 3, 5, 8, 14, 25]
coin_types1 = [1, 5, 10, 25]
changegoal = 74
print(greedy_change_make(157, coin_types1))

