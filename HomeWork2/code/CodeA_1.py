import time


def read_matrix_from_file(filename):
    with open(filename, 'r') as f:
        matrix = [list(map(int, line.split())) for line in f]
    return matrix


def find_max_blank_square_brute_force(matrix, L):
    M = len(matrix)
    N = len(matrix[0])
    max_count = -1
    max_position = (-1, -1)
    
    for i in range(M - L + 1):
        for j in range(N - L + 1):
            count = 0
            for k in range(i, i + L):
                for l in range(j, j + L):
                    if matrix[k][l] == 0:
                        count += 1
            if count > max_count:
                max_count = count
                max_position = (i + 1, j + 1)
    
    return max_position, max_count


def main():
    filename = "HomeWork2/code/dataset_a/Matrix_500_500.txt"
    L = int(input("请输入L: "))
    
    matrix = read_matrix_from_file(filename)
    
    print("使用测试数据 " + filename + " 进行测试...")
    print("使用暴力搜索算法...")

    start_time = time.time()

    brute_force_position = find_max_blank_square_brute_force(matrix, L)

    brute_force_time = time.time() - start_time

    print(f"暴力搜索算法找到的最大空白子矩阵左上角坐标: {brute_force_position[0]}")
    print(f"最大空白方格数为: {brute_force_position[1]}")
    print(f"暴力搜索算法运行时间: {brute_force_time:.6f} 秒")
    
if __name__ == "__main__":
    main()
