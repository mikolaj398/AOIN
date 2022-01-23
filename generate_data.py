import random
import os
num_rows = 200
max_value = 50
max_weight = 200

def generate(num_of_files):
    for file in os.listdir('data/'):
       os.remove(f'data/{file}') 

    for index in range(num_of_files):
        lines = []
        weight_sum = 0
        for line in range(num_rows):
            weight = random.randint(1, max_weight)
            value = random.randint(0, max_value)

            lines.append(f"{weight}, {value}")

            weight_sum += weight

        with open(f'data/data{index}.txt', 'w+') as f:
            f.write(str(random.randint(100, round(weight_sum * 0.3))) + '\n')
            f.write('\n'.join(lines))