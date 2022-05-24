num1 = int(input())
num2 = int(input())
num3 = int(input())

for x1 in range(1, num1 + 1):
    for x2 in range(1, num2 + 1):
        for x3 in range(1, num3 + 1):
            if x1 % 2 == 0 and (x2 == 2 or x2 == 3 or x2 == 5 or x2 == 7) and x3 % 2 == 0:
                print(f'{x1} {x2} {x3}')