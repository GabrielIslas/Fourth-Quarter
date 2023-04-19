
def activity_selection(activities):
    selected_activities = []
    activities.sort(key = lambda x: x[1])
    i = 0
    selected_activities.append(activities[0])
    for j in range(1, len(activities)):
        if activities[j][0] >= activities[i][1]:
            selected_activities.append(activities[j])
            i = j
    return selected_activities

activities1 = [(5,9), (1,2), (3,4), (0,6), (5,7), (8,9)]
print(activity_selection(activities1))