# if activities[i][1] > activities[j][0] and activities[i][0] <= activities[j][1]
def define_halls(activities):
    halls = []
    activities.sort()
    for activity in activities:
        hallindex = find_hall(activity, halls)
        if hallindex == -1:
            newhall = [activity]
            halls.append(newhall)
        else:
            halls[hallindex].append(activity)
    return halls
        
def find_hall(activity, halls):
    for i in range(len(halls)):
        if not collision(activity, halls[i]):
            return i
    return -1
        
def collision(activity, hall):
    if activity[1] > hall[-1][0] and activity[0] <= hall[-1][1]:
        return True
    return False

activities1 = [(1,3), (1,5), (1,2), (4,6), (4,8), (7,10), (7,11), (12, 14), (12, 15)]
print(define_halls(activities1))
