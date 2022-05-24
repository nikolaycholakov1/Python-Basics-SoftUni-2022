max_capacity = float(input())

input_line = input()
max_capacity_copy = max_capacity
capacity_left = max_capacity
suitcase_counter = 0

while input_line != 'End':
    suitcase_volume = float(input_line)

    if capacity_left < suitcase_volume:
        break
    suitcase_counter += 1

    if suitcase_counter % 3 == 0:
        suitcase_volume = suitcase_volume * 1.10

    capacity_left = capacity_left - suitcase_volume

    input_line = input()

if input_line == 'End':
    print(f"Congratulations! All suitcases are loaded!")
    print(f"Statistic: {suitcase_counter} suitcases loaded.")
else:
    print(f"No more space!")
    print(f"Statistic: {suitcase_counter} suitcases loaded.")