import time

def read_hypergraph(filename):
    hypergraph = []
    with open(filename, 'r') as file:
        for line in file:
            edge = set(line.strip().split())
            hypergraph.append(edge)
    return hypergraph

def is_cover(hypergraph, vertex_cover):
    for edge in hypergraph:
        if not edge & vertex_cover:
            return False
    return True

def greedy_vertex_cover(hypergraph):
    cover = set()
    edges = set(map(frozenset, hypergraph))
    while edges:
        v = max(set().union(*edges), key=lambda x: sum(x in e for e in edges))
        cover.add(v)
        edges = {e for e in edges if v not in e}
    return cover

def save_vertex_cover(filename, vertex_cover):
    with open(filename, 'w') as file:
        file.write(" ".join(vertex_cover))

def main(filename, output_filename):
    hypergraph = read_hypergraph(filename)
    start_time = time.time()
    minimal_cover = greedy_vertex_cover(hypergraph)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    minimal_cover = sorted(list(minimal_cover), key=int)

    # Save minimal vertex cover to file
    save_vertex_cover(output_filename, minimal_cover)

    print("Size of  minimal vertex cover:", len(minimal_cover))

    return minimal_cover

# Example usage
hypergraph_filename = 'FinalAssignment/code/dataset_B/cryg10000.txt'
output_filename = 'FinalAssignment/code/dataset_B/minimal_cover.txt'
minimal_cover = main(hypergraph_filename, output_filename)
print("The minimal vertex cover is:", minimal_cover)