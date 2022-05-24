number = int(input())

happy_number = 0

for x1 in range(1, number + 1):
    for x2 in range(1, number + 1):
        for x3 in range(1, number + 1):
            for x4 in range(1, number + 1):
                if x1 + x2 == x3 + x4 and number % x1 + x2 == 1:
                    x11 = x1
                    x22 = x2
                    x33 = x3
                    x44 = x4
                    print(f'{x11}{x22}{x33}{x44}', end=' ')