import random

def generate_hypergraph(num_vertices, num_edges, min_edge_size, max_edge_size, filename):
    with open(filename, 'w') as file:
        for _ in range(num_edges):
            edge_size = random.randint(min_edge_size, max_edge_size)
            edge = random.sample(range(1, num_vertices + 1), edge_size)
            file.write(" ".join(map(str, edge)) + "\n")

# Parameters for the hypergraph
num_vertices = 25
num_edges = 10
min_edge_size = 2
max_edge_size = 5
filename = 'FinalAssignment/code/dataset_B/min_35_10.txt'

# Generate the hypergraph
generate_hypergraph(num_vertices, num_edges, min_edge_size, max_edge_size, filename)
