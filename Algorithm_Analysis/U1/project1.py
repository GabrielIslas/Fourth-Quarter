from pathlib import Path
import numpy as np
import math
import networkx as nx
import matplotlib.pyplot as plt

filename = "testfile.txt"
filepath = Path(__file__).with_name(filename)

def read_graph(file_path: Path):
    stringList = []
    with open(file_path) as f:
        for line in f:
            stringList.append(line.strip())
    tupleList = []
    for string in stringList:
        tupleList.append(tuple(int(element) for element in string.split()))
    return tupleList

def get_adjacency_matrix(edge_list: list):
    existingNodes = set() 
    for edge in edge_list: # add all nodes to set
        existingNodes.add(edge[0])
        existingNodes.add(edge[1])
    matrixSize = len(existingNodes) # sets can't have repeats
    adjacency_matrix = np.full((matrixSize, matrixSize), math.inf, float)
    for edge in edge_list:
        adjacency_matrix[edge[0] - 1][edge[1] - 1] = edge[2]
        adjacency_matrix[edge[1] - 1][edge[0] - 1] = edge[2]
    for index in range(matrixSize):
        adjacency_matrix[index][index] = 0
    return adjacency_matrix

def get_distance_matrix(adjacency_matrix: np.ndarray):
    # pdm : previous distance matrix
    # cdm : current distance matrix
    rowNumber = adjacency_matrix.shape[0]
    pdm = 0
    cdm = adjacency_matrix
    for k in range(rowNumber):
        pdm = cdm
        for i in range(rowNumber):
            for j in range(rowNumber):
                cdm[i][j] = min(pdm[i][j], pdm[i][k] + pdm[k][j])
    return cdm

def get_average_path_length(distance_matrix: np.ndarray):
    return np.average(distance_matrix)

def get_diameter(distance_matrix: np.ndarray):
    return np.max(distance_matrix)

def get_eccentricity(distance_matrix: np.ndarray, node:int):
    return np.max(distance_matrix[node-1])

def get_radius(distance_matrix: np.ndarray):
    return min([get_eccentricity(distance_matrix, i) for i in range(distance_matrix.shape[0])])

def get_periphery(distance_matrix: np.ndarray):
    periphery_set = set()
    rowAmount = distance_matrix.shape[0]
    diameter = get_diameter(distance_matrix)
    for row in range(rowAmount):
        if get_eccentricity(distance_matrix, row + 1) == diameter:
            periphery_set.add(row + 1)
    return periphery_set

def get_center(distance_matrix: np.ndarray):
    center_set = set()
    rowAmount = distance_matrix.shape[0]
    radius = get_radius(distance_matrix)
    for row in range(rowAmount):
        if get_eccentricity(distance_matrix, row + 1) == radius:
            center_set.add(row + 1)
    return center_set

def create_graph(edge_list: list):
    existingNodes = set() 
    for edge in edge_list: # add all nodes to set
        existingNodes.add(edge[0])
        existingNodes.add(edge[1])
    graph = nx.Graph()
    graph.add_nodes_from(existingNodes)
    graph.add_weighted_edges_from(edge_list)
    return graph
        
graphList = read_graph(filepath)
print("Edge list from file:")
print(graphList)
adjacency_matrix = get_adjacency_matrix(graphList)
print("\nAdjacency matrix:")
print(adjacency_matrix)
print("\nDistance matrix:")
distance_matrix = get_distance_matrix(adjacency_matrix)
print(distance_matrix)
print(f"Average path length: {get_average_path_length(distance_matrix)}")
print(f"Diameter: {get_diameter(distance_matrix)}")
print(f"Eccentricity of node 1: {get_eccentricity(distance_matrix, 1)}")
print(f"Eccentricity of node 2: {get_eccentricity(distance_matrix, 2)}")
print(f"Eccentricity of node 3: {get_eccentricity(distance_matrix, 3)}")
print(f"Eccentricity of node 4: {get_eccentricity(distance_matrix, 4)}")
print(f"Eccentricity of node 5: {get_eccentricity(distance_matrix, 5)}")
print(f"Eccentricity of node 6: {get_eccentricity(distance_matrix, 6)}")
print(f"Eccentricity of node 7: {get_eccentricity(distance_matrix, 7)}")
print(f"Eccentricity of node 8: {get_eccentricity(distance_matrix, 8)}")
print(f"Radius: {get_radius(distance_matrix)}")
print(f"Periphery set: {get_periphery(distance_matrix)}")
print(f"Center set: {get_center(distance_matrix)}")
graphStructure = create_graph(graphList)
position = nx.spring_layout(graphStructure)
nx.draw_networkx(graphStructure, pos=position, arrows = False, with_labels = True)
labels = nx.get_edge_attributes(graphStructure, "weight")
nx.draw_networkx_edge_labels(graphStructure, position, edge_labels=labels)
plt.show()



    

      