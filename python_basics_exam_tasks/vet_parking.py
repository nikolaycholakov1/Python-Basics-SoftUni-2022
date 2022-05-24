days = int(input())
hours = int(input())

total_sum = 0

for day in range(1, days + 1):
    parking_tax = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            parking_tax += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            parking_tax += 1.25
        else:
            parking_tax += 1
    total_sum += parking_tax

    print(f'Day: {day} - {parking_tax:.2f} leva')
print(f"Total: {total_sum:.2f} leva")

