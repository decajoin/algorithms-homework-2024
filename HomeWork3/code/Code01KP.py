import time

# 读取数据集
def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        data = [tuple(map(int, line.split())) for line in lines[0:]]
        return data

# 使用贪心算法解决01背包问题
def greedy_knapsack(items, capacity):
    # 计算每个物品的单位价值（即每单位重量的价值）
    value_per_weight = [(item[0] / item[1], item[0], item[1]) for item in items]
    # 按单位价值降序排序
    value_per_weight.sort(reverse=True)

    # 贪心选择物品放入背包
    knapsack = []
    total_value = 0
    remaining_capacity = capacity
    # 选择单位价值最高的物品，直到背包容量不足为止（贪心思想体现）
    for value_per_unit, value, weight in value_per_weight:
        if remaining_capacity >= weight:
            knapsack.append((value, weight))
            total_value += value
            remaining_capacity -= weight

    return knapsack, total_value

if __name__ == "__main__":
    # 读取数据集
    filename = "HomeWork3\code\dataset_01KP\low-dimensional\\f8_l-d_kp_23_10000"
    items = read_data(filename)

    # 移除数据集中的第一行，并获取物品数量和背包容量
    n, capacity = items.pop(0)

    # 计算执行时间
    start_time = time.time()

    # 使用贪心算法解决01背包问题
    knapsack, total_value = greedy_knapsack(items, capacity)

    # 计算执行时间
    execution_time = time.time() - start_time

    # 打印结果
    print("使用数据集" + filename + "进行测试")
    print("从背包中选择的物品如下:")
    for item in knapsack:
        print("价值:", item[0], "重量:", item[1])
    print("总价值:", total_value)
    print("执行时间:", execution_time, "秒")