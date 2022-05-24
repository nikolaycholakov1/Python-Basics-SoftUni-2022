price_over_20kg = float(input())
luggage_weight = float(input())
days_to_departure = int(input())
luggage_count = int(input())

price_below_20kg = price_over_20kg
final_price = 0
price_increase = 0

if luggage_weight < 10:
    price_below_20kg = price_over_20kg * 0.20
elif luggage_weight < 20:
    price_below_20kg = price_over_20kg * 0.50
elif luggage_weight > 20:
    price_below_20kg = price_over_20kg

if days_to_departure < 7:
    price_increase = 1.40
elif days_to_departure <= 30:
    price_increase = 1.15
elif days_to_departure > 30:
    price_increase = 1.10


if luggage_weight <= 20:
    final_price = (price_below_20kg * luggage_count) * price_increase
elif luggage_weight > 20:
    final_price = (price_over_20kg * luggage_count) * price_increase


print(f" The total price of bags is: {final_price:.2f} lv. ")