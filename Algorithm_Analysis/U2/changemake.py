# Dynamic programming
# Step 1. Define objective function
# Step 2. Define base case
# Step 3. Define recurrence

import math

coin_types = [1,3,4]
changegoal = 38

def change_make(change, coins):
    F = [0]
    coinGroups = []
    for i in range(1, change+1):
        temp = math.inf
        j = 0
        coinGroup = []
        while j < len(coins) and i >= coins[j]:
            if(F[i - coins[j]] < temp):
                coinGroup.append(coins[j])
            temp = min(F[i - coins[j]], temp)
            j += 1
        coinGroups.append(coinGroup)
        F.append(temp+1)
    tempchange = change
    index = change - 1
    coinsUsed = []
    while tempchange != 0:
        lastValue = coinGroups[index][len(coinGroups[index]) - 1]
        coinsUsed.append(lastValue)
        index -= lastValue
        tempchange -= lastValue
    print(F)
    print(coinsUsed)
    return F[change]

print(change_make(changegoal, coin_types))

