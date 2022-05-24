budget = float(input())
fuel_count = float(input())
day = input()

final_price = (fuel_count * 2.10) + 100

if day == 'Saturday':
    final_price *= 0.90
elif day == 'Sunday':
    final_price *= 0.80

if budget >= final_price:
    print(f"Safari time! Money left: {budget - final_price:.2f} lv. ")
elif budget < final_price:
    print(f"Not enough money! Money needed: {abs(budget - final_price):.2f} lv.")