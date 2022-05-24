import math

fan_name = input()
budget = float(input())
beers = int(input())
chips_bags = int(input())

all_beers_price = beers * 1.20
chips_bags_price = math.ceil((all_beers_price * 0.45) * chips_bags)
total_sum = all_beers_price + chips_bags_price
diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"{fan_name} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{fan_name} needs {diff:.2f} more leva!")