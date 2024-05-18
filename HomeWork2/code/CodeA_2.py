import time



def read_matrix_from_file(filename):
    with open(filename, 'r') as f:
        matrix = [list(map(int, line.split())) for line in f]
    return matrix



def find_max_blank_square_prefix_sum(matrix, L):
    M = len(matrix)
    N = len(matrix[0])
    
    prefix_sum = [[0] * (N + 1) for _ in range(M + 1)]
    
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + (1 if matrix[i-1][j-1] == 0 else 0)
    
    max_count = -1
    max_position = (-1, -1)
    
    for i in range(M - L + 1):
        for j in range(N - L + 1):
            total = prefix_sum[i+L][j+L] - prefix_sum[i][j+L] - prefix_sum[i+L][j] + prefix_sum[i][j]
            if total > max_count:
                max_count = total
                max_position = (i + 1, j + 1)
    
    return max_position, max_count



def main():
    filename = "HomeWork2/code/dataset_a/Matrix_500_500.txt" 
    L = int(input("请输入L: "))
    
    matrix = read_matrix_from_file(filename)
    
    print("使用测试数据 " + filename + " 进行测试...")
    print("使用滑动窗口 + 前缀和算法...")

    start_time = time.time()

    prefix_sum_position = find_max_blank_square_prefix_sum(matrix, L)

    prefix_sum_time = time.time() - start_time

    print(f"滑动窗口 + 前缀和算法找到的最大空白子矩阵左上角坐标: {prefix_sum_position[0]}")
    print(f"最大空白方格数为: {prefix_sum_position[1]}")
    print(f"滑动窗口 + 前缀和算法运行时间: {prefix_sum_time:.6f} 秒")

if __name__ == "__main__":
    main()
