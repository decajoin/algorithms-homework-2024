import math
import itertools

# 计算两点之间的欧氏距离
def distance(coord1, coord2):
    return math.sqrt((coord1[1] - coord2[1])**2 + (coord1[2] - coord2[2])**2)

# 读取数据集
def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        coords = []
        start_reading = False
        for line in lines:
            if line.startswith('NODE_COORD_SECTION'):
                start_reading = True
                continue
            if start_reading and not line.startswith('EOF'):
                parts = line.split()
                coords.append((int(parts[0]), float(parts[1]), float(parts[2])))
        return coords

# 暴力算法解决旅行商问题
def brute_force_tsp(coords):
    n = len(coords)
    all_permutations = itertools.permutations(range(1, n))
    min_path = None
    min_distance = float('inf')

    def total_distance(path):
        dist = 0
        for i in range(len(path) - 1):
            dist += distance(coords[path[i]], coords[path[i+1]])
        dist += distance(coords[path[-1]], coords[path[0]])
        return dist

    for perm in all_permutations:
        current_path = [0] + list(perm)
        current_distance = total_distance(current_path)
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = current_path

    min_path.append(0)
    return [coords[i][0] for i in min_path]

if __name__ == "__main__":
    # 读取数据集
    filename = "HomeWork4/code/dataset_TSP/small_dataset.tsp"
    coords = read_data(filename)

    # 使用暴力算法解决旅行商问题
    path = brute_force_tsp(coords)

    # 打印路径
    print("使用数据集" + filename + "进行测试")
    print("最佳路径:", path)
