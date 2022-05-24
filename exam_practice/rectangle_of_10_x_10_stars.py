symbol = '*'
counter_row = 0
counter_col = 0

for row in range (1, 12):
    counter_row += 1

    if counter_row == 11:
        break

    for col in range(1, 11):
        counter_col += 1
        print(symbol, end='')
        if counter_col == 10:
            break
    print()
