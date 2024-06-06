import time

def read_data_knapsack(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        data = [tuple(map(int, line.split())) for line in lines[0:]]
        return data

def knapsack_brute_force(items, capacity):
    n = len(items)
    # 生成所有可能的选择方案
    all_combinations = []
    for i in range(2**n):
        combination = []
        for j in range(n):
            if (i >> j) & 1:
                combination.append(items[j])
        all_combinations.append(combination)

    # 遍历所有选择方案，找到最优解
    best_value = 0
    best_combination = []
    for combination in all_combinations:
        total_value = 0
        total_weight = 0
        for item in combination:
            total_value += item[0]
            total_weight += item[1]
        if total_weight <= capacity and total_value > best_value:
            best_value = total_value
            best_combination = combination

    return best_combination, best_value

if __name__ == "__main__":
    # 读取数据集
    filename = "HomeWork4\code\dataset_01KP\low-dimensional\\f8_l-d_kp_23_10000"
    items = read_data_knapsack(filename)
    n, capacity = items.pop(0)  # 移除数据集中的第一行，并获取物品数量和背包容量

    # 计算时间
    start_time = time.time()

    # 使用暴力穷举算法解决01背包问题
    knapsack, total_value = knapsack_brute_force(items, capacity)

    # 计算时间
    execution_time = time.time() - start_time

    # 打印结果
    print("使用数据集" + filename + "进行测试")
    print("从背包中选择的物品如下:")
    for item in knapsack:
        print("价值:", item[0], "重量:", item[1])
    print("总价值:", total_value)
    print("执行时间:", execution_time, "秒")