from pathlib import Path
import numpy as np

filename = "testfile.txt"
filepath = Path(__file__).with_name(filename)

def read_graph(file_path):
    stringList = []
    with open(file_path) as f:
        for line in f:
            stringList.append(line.strip())
    tupleList = []
    for string in stringList:
        tupleList.append(tuple(int(element) for element in string.split()))
    return tupleList

def get_adjacency_matrix(edge_list):
    existingNodes = set() 
    for edge in edge_list: # add all nodes to set
        existingNodes.add(edge[0])
        existingNodes.add(edge[1])
    matrixSize = len(existingNodes) # sets can't have repeats
    adjacency_matrix = np.zeros((matrixSize, matrixSize), int)
    for edge in edge_list:
        adjacency_matrix[edge[0] - 1][edge[1] - 1] = edge[2]
        adjacency_matrix[edge[1] - 1][edge[0] - 1] = edge[2]
    return adjacency_matrix

graphList = read_graph(filepath)
print(graphList)
adjacency_matrix = get_adjacency_matrix(graphList)
print(adjacency_matrix)
    

      