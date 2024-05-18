import random

def generate_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(0, 1) for _ in range(cols)]
        matrix.append(row)
    return matrix

def save_matrix_to_file(matrix, filename):
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')

def main():
    rows = int(input("请输入矩阵的行数: "))
    cols = int(input("请输入矩阵的列数: "))

    filename = "HomeWork2/code/dataset_a/Matrix_500_500.txt"

    matrix = generate_matrix(rows, cols)
    save_matrix_to_file(matrix, filename)
    print(f"矩阵已保存到 {filename}")

if __name__ == "__main__":
    main()
