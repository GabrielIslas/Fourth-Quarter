
def coinrow(C):
    F = [0, C[0]] # starting values
    coinsUsed = []
    coinList = [C[0]]
    for i in range(1, len(C)): # save the best sums so far
        if(C[i] + F[i-1] > F[i]):
            F.append(C[i] + F[i-1])
            coinList.append(C[i])
        else:
            F.append(F[i])
            coinsUsed.extend(reversed(coinList[::-2]))
            coinList.clear()
    coinsUsed.extend(reversed(coinList[::-2]))
    return (F.pop(), coinsUsed)

coinlist = [5,1,2,10,6,2,4,5,1,8,3,1,9]

print(coinrow(coinlist))


