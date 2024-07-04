def read_hypergraph(filename):
    hypergraph = []
    with open(filename, 'r') as file:
        for line in file:
            edge = set(line.strip().split())
            hypergraph.append(edge)
    return hypergraph

def verify_vertex_cover(hypergraph, vertex_cover):
    for edge in hypergraph:
        if not edge & vertex_cover:
            return False
    return True

def main():
    hypergraph_filename = 'FinalAssignment/code/dataset_B/circuit_3.txt'
    minimal_cover_filename = 'FinalAssignment/code/dataset_B/minimal_cover.txt'

    hypergraph = read_hypergraph(hypergraph_filename)

    # Read minimal vertex cover from file
    with open(minimal_cover_filename, 'r') as file:
        minimal_cover = set(file.read().strip().split())

    # Verify if the minimal cover is indeed a vertex cover
    if verify_vertex_cover(hypergraph, minimal_cover):
        print("The minimal vertex cover is valid.")
    else:
        print("The minimal vertex cover is not valid.")

if __name__ == "__main__":
    main()
