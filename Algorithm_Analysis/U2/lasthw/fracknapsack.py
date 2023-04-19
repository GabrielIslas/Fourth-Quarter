# item (value, weight)
def fknapsack(capacity, items):
    items.sort(key = lambda x: (x[0]/x[1]), reverse = True)
    result = 0.0
    for item in items:
        if item[1] <= capacity:
            capacity -= item[1]
            result += item[0]
        else:
            capacity -= capacity / item[1]
            result += item[0] * capacity / item[1]
    return result
# item (value, weight)
capacity1 = 50
items1 = [(60, 10), (100, 20), (120, 30)]
print(fknapsack(capacity1, items1))