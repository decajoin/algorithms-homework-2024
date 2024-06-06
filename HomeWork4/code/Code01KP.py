import time

def read_data_knapsack(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        data = [tuple(map(int, line.split())) for line in lines[0:]]
        return data

def knapsack_dp(items, capacity):
    n = len(items)
    # dp[i][w] 表示前 i 个物品在容量为 w 时的最大价值
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    # 找到哪些物品被放入背包
    w = capacity
    knapsack = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            knapsack.append(items[i - 1])
            w -= items[i - 1][1]

    total_value = dp[n][capacity]
    return knapsack, total_value

if __name__ == "__main__":
    # 读取数据集
    filename = "HomeWork4\code\dataset_01KP\low-dimensional\\f8_l-d_kp_23_10000"
    items = read_data_knapsack(filename)
    n, capacity = items.pop(0)  # 移除数据集中的第一行，并获取物品数量和背包容量

    # 计时开始
    start_time = time.time()

    # 使用动态规划算法解决01背包问题
    knapsack, total_value = knapsack_dp(items, capacity)

    # 计时结束
    execution_time = time.time() - start_time

    # 打印结果
    print("使用数据集" + filename + "进行测试")
    print("从背包中选择的物品如下:")
    for item in knapsack:
        print("价值:", item[0], "重量:", item[1])
    print("总价值:", total_value)
    print("执行时间:", execution_time, "秒")