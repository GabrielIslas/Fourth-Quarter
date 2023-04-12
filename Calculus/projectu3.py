import math

def tk(k):
    sum = 0
    for i in range(1, k+1):
        sum += 1/i
    result = sum - math.log(k)
    return result

def tkc(values):
    for value in values:
        print(tk(value))
        
def ec(k):
    return tk(k) - (1/k)
  
def ecc(values):
    for value in values:
        print(ec(value))
        
values1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
values2 = [20, 30, 40, 50, 60, 70, 80, 90, 100]
values3 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
values4 = [10000, 100000, 1000000, 10000000]

tkc(values4)
ecc(values4)

