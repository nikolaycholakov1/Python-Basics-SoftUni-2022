num1 = input()
num2 = input()

start1 = num1[0]
start2 = num1[1]
start3 = num1[2]
start4 = num1[3]

end1 = num2[0]
end2 = num2[1]
end3 = num2[2]
end4 = num2[3]

for x1 in range(int(start1), int(end1) + 1):
    for x2 in range(int(start2), int(end2) + 1):
        for x3 in range(int(start3), int(end3) + 1):
            for x4 in range(int(start4), int(end4) + 1):
                if x1 % 2 != 0 and x2 % 2 != 0 and x3 % 2 != 0 and x4 % 2 != 0:
                    print(f"{x1}{x2}{x3}{x4}", end=' ')