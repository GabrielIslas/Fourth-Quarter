def interval_graph(activities):
    size = len(activities)
    adjacency_list = []
    for i in range(size):
        node_list = []
        for j in range(size):
            if activities[i][1] > activities[j][0] and activities[i][0] <= activities[j][1] and i != j:
                node_list.append((j, activities[j]))
        adjacency_list.append(node_list)
    return adjacency_list

def coloring(adjacency_list):
    colors = [0] * len(adjacency_list)
    

activities1 = [(1,3), (1,5), (1,2), (4,6), (4,8), (7,10), (7,11), (12, 14), (12, 15)]

list1 = interval_graph(activities1)
print(list1)