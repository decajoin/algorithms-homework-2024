import math
import sys
sys.setrecursionlimit(3000)

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

# 动态规划算法解决旅行商问题
def dp_tsp(coords):
    n = len(coords)
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist[i][j] = distance(coords[i], coords[j])

    memo = {}

    def tsp(mask, pos):
        if mask == (1 << n) - 1:
            return dist[pos][0]
        if (mask, pos) in memo:
            return memo[(mask, pos)]

        ans = float('inf')
        for city in range(n):
            if mask & (1 << city) == 0:
                ans = min(ans, dist[pos][city] + tsp(mask | (1 << city), city))
        memo[(mask, pos)] = ans
        return ans

    def find_path():
        mask = 1
        pos = 0
        path = [0]
        while mask != (1 << n) - 1:
            next_city = None
            best_dist = float('inf')
            for city in range(n):
                if mask & (1 << city) == 0:
                    curr_dist = dist[pos][city] + memo.get((mask | (1 << city), city), float('inf'))
                    if curr_dist < best_dist:
                        best_dist = curr_dist
                        next_city = city
            if next_city is None:
                raise ValueError(f"Failed to find next city from position {pos} with mask {mask}")
            path.append(next_city)
            pos = next_city
            mask |= (1 << next_city)
        path.append(0)
        return [coords[i][0] for i in path]

    tsp(1, 0)
    return find_path()

if __name__ == "__main__":
    # 读取数据集
    filename = "HomeWork4/code/dataset_TSP/small_dataset.tsp"
    coords = read_data(filename)

    # 使用动态规划算法解决旅行商问题
    path = dp_tsp(coords)

    # 打印路径
    print("使用数据集" + filename + "进行测试")
    print("最佳路径:", path)
