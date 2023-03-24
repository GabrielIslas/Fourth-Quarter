pointlist = [(0,3),(2,2),(1,1),(2,1),(3,0),(0,0),(3,3)]
pointlist = sorted(pointlist)

def convexhull_r(points: list):
    if len(points) == 1:
        return points
    
    left_points = convexhull_r(points[:len(points)//2])
    right_points = convexhull_r(points[len(points)//2 + 1:])
    print(left_points)
    print(right_points)
    left_points.extend(right_points)
    return left_points

print(pointlist)

print(convexhull_r(pointlist))






