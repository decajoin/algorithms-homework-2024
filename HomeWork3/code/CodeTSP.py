import math

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

# 贪心算法解决旅行商问题
def greedy_tsp(coords):
    num_cities = len(coords)
    visited = [False] * num_cities
    path = []
    
    # 选择起始点
    current_city = coords[0]
    path.append(current_city[0])
    visited[0] = True
    
    # 逐步选择下一个城市
    for _ in range(num_cities - 1):
        min_dist = float('inf')
        nearest_city = None
        # 选择离当前城市最近的未访问的城市（贪心思想体现）
        for i in range(num_cities):
            if not visited[i]:
                dist = distance(current_city, coords[i])
                if dist < min_dist:
                    min_dist = dist
                    nearest_city = coords[i]
        path.append(nearest_city[0])
        current_city = nearest_city
        visited[current_city[0] - 1] = True
        
    # 回到起点
    path.append(path[0])
    
    return path

if __name__ == "__main__":
    # 读取数据集
    filename = "HomeWork3\code\dataset_TSP\mu1979.tsp"
    coords = read_data(filename)
    
    # 使用贪心算法解决旅行商问题
    path = greedy_tsp(coords)
    
    # 打印路径
    print("使用数据集" + filename + "进行测试")
    print("最佳路径:", path)
