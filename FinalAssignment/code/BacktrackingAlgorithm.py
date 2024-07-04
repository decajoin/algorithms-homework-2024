import time

def read_hypergraph(filename):
    hypergraph = []
    with open(filename, 'r') as file:
        for line in file:
            edge = set(line.strip().split())
            hypergraph.append(edge)
    return hypergraph

def is_cover(hypergraph, vertex_cover):
    return all(bool(edge & vertex_cover) for edge in hypergraph)

def find_minimal_covers(hypergraph):
    all_vertices = sorted(list(set.union(*hypergraph)), key=int)
    minimal_covers = []

    def backtrack(index, current_cover):
        if index == len(all_vertices):
            if is_cover(hypergraph, current_cover):
                if all(not is_cover(hypergraph, current_cover - {v}) for v in current_cover):
                    minimal_covers.append(set(current_cover))
            return

        vertex = all_vertices[index]

        # 不包含当前顶点
        backtrack(index + 1, current_cover)

        # 包含当前顶点
        current_cover.add(vertex)
        backtrack(index + 1, current_cover)
        current_cover.remove(vertex)

    backtrack(0, set())
    return minimal_covers

def save_vertex_cover(filename, vertex_cover):
    with open(filename, 'w') as file:
        file.write(" ".join(sorted(vertex_cover, key=int)))

def main(hypergraph_filename, output_filename):
    hypergraph = read_hypergraph(hypergraph_filename)

    start_time = time.time()
    minimal_covers = find_minimal_covers(hypergraph)
    end_time = time.time()

    print(f"Time taken: {end_time - start_time:.4f} seconds")


    # 选择第一个极小顶点覆盖（或者可以选择最小的那个）
    minimal_cover = min(minimal_covers, key=len)
    minimal_cover = sorted(list(minimal_cover), key=int)

    # 保存极小顶点覆盖到文件
    save_vertex_cover(output_filename, minimal_cover)

    print("Size of minimal vertex cover:", len(minimal_cover))
    return minimal_cover


# 示例使用
hypergraph_filename = 'FinalAssignment/code/dataset_B/min.txt'
output_filename = 'FinalAssignment/code/dataset_B/minimal_cover.txt'
minimal_cover = main(hypergraph_filename, output_filename)
if minimal_cover:
    print("The minimal vertex cover is:", minimal_cover)