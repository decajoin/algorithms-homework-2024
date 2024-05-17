import random

def generate_random_numbers(quantity, file_path):
    random_numbers = set()

    while len(random_numbers) < quantity:
        random_numbers.add(random.randint(1, 1000000000000))

    with open(file_path, 'w') as file:
        file.write(' '.join(map(str, random_numbers)))

    print(f'Successfully generated {quantity} random numbers in {file_path}.')

# 示例用法
quantity = int(input("请输入要生成的随机数的数量："))
generate_random_numbers(quantity, "HomeWork2/code/dataset_a/Number_1e7.txt")