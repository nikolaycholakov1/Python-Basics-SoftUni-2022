n = int(input())
m = int(input())
s = int(input())

for i in range(1, n):
    for j in range (1, 10):
        for k in range (1, m):
                if i % 2 == 0 and k % 2 == 0:
                    print(f'{i}{k}', end=' ')