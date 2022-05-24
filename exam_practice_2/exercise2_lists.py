list = [[1, 2],[3,4]]
m = 1
print(list)
for i in range(0, 2):
    m *= 10
    for j in range(0, 2):
        list[i][j] *= m
print(list)