from functools import cmp_to_key

middle = [0, 0]

def quadrant(point: list):
    if point[0] >= 0 and point[1] >= 0:
        return 1
    if point[0] <= 0 and point[1] >= 0:
        return 2
    if point[0] <= 0 and point[1] <= 0:
        return 3
    return 4

def orientation(point1: list, point2: list, point3: list):
    result = (point2[1]-point1[1]) * (point3[0]-point2[0]) - (point3[1]-point2[1]) * (point2[0]-point1[0])
    if result == 0:
        return 0
    if result > 0:
        return 1
    return -1

def point_comparison(point1: list, point2: list):
    point1m = [point1[0] - middle[0], point1[1] - middle[1]]
    point2m = [point2[0] - middle[0], point2[1] - middle[1]]
    point1quadrant = quadrant(point1m)
    point2quadrant = quadrant(point2m)
    if point1quadrant != point2quadrant:
        if point1quadrant < point2quadrant:
            return -1
        return 1
    if point1m[1]*point2m[0] < point2m[1] * point1m[0]:
        return -1
    return 1

def hull_merger(polygon1: list, polygon2: list):
    points1, points2 = len(polygon1), len(polygon2)
    lpoint1, lpoint2 = 0, 0
    
    for i in range(1, points1):
        if polygon1[i][0] > polygon1[lpoint1][0]:
            lpoint1 = i
            
    for i in range(1, points2):
        if polygon2[i][0] < polygon2[lpoint2][0]:
            lpoint2 = i
    
    temp1, temp2 = lpoint1, lpoint2
    done = False
    while not done:
        done = True
        while orientation(polygon2[temp2], polygon1[temp1], polygon1[(temp1 + 1) % points1]) >= 0:
            temp1 = (temp1 + 1) % points1
        while orientation(polygon1[temp1], polygon2[temp2], polygon2[(points2 + temp2 - 1) % points2]) <= 0:
            temp2 = (temp2 + 1) % points2
            done = False            
    uppert1, uppert2 = temp1, temp2
    
    temp1, temp2 = lpoint1, lpoint2
    done = False
    while not done:
        done = True
        while orientation(polygon1[temp1], polygon2[temp2], polygon2[(temp2 + 1) % points2]) >= 0:
            temp2 = (temp2 + 1) % points2
        while orientation(polygon2[temp2], polygon1[temp1], polygon1[(points1 + temp1 - 1) % points1]) <= 0:
            temp1 = (temp1 + 1) % points1
            done = False
    lowert1, lowert2 = temp1, temp2
    
    mergedHull = []
    index = uppert1
    mergedHull.append(polygon1[uppert1])
    while index != lowert1:
        index = (index + 1) % points1
        mergedHull.append(polygon1[index])
        
    index = lowert2
    mergedHull.append(polygon2[lowert2])
    while index != uppert2:
        index = (index + 1) % points2
        mergedHull.append(polygon2[index])
        
    return mergedHull

def bruteHull(a):
    global middle
    s = set()
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            x1, x2 = a[i][0], a[j][0]
            y1, y2 = a[i][1], a[j][1]
            a1, b1, c1 = y1-y2, x2-x1, x1*y2-y1*x2
            pos, neg = 0, 0
            for k in range(len(a)):
                if a1*a[k][0]+b1*a[k][1]+c1 <= 0:
                    neg += 1
                if a1*a[k][0]+b1*a[k][1]+c1 >= 0:
                    pos += 1
            if pos == len(a) or neg == len(a):
                s.add(tuple(a[i]))
                s.add(tuple(a[j]))
    ret = []
    for x in s:
        ret.append(list(x))
    middle = [0, 0]
    n = len(ret)
    for i in range(n):
        middle[0] += ret[i][0]
        middle[1] += ret[i][1]
        ret[i][0] *= n
        ret[i][1] *= n
    ret = sorted(ret, key=cmp_to_key(point_comparison))
    for i in range(n):
        ret[i] = [ret[i][0]/n, ret[i][1]/n]
    return ret
    
def convex_hull(points):
    if len(points) <= 5:
        return bruteHull(points)
    
    left, right = [], []
    start = int(len(points) / 2)
    for i in range(start):
        left.append(points[i])
    for i in range(start, len(points)):
        right.append(points[i])
    
    left_hull = convex_hull(left)
    right_hull = convex_hull(right)
    
    return hull_merger(left_hull, right_hull)
        
    
a = []
a.append([0, 0])
a.append([1, -4])
a.append([-1, -5])
a.append([-5, -3])
a.append([-3, -1])
a.append([-1, -3])
a.append([-2, -2])
a.append([-1, -1])
a.append([-2, -1])
a.append([-1, 1])
a.sort()

print(convex_hull(a))
 






