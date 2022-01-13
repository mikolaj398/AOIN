import random

num_rows = 200
max_value = 50
max_weight = 200
for index in range(20):
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

        

