pastry = input()
pastries_ordered = int(input())
day_of_month = int(input())

cake_price = 0
souffle_price = 0
baklava_price = 0
discount = 0

if pastry == 'Cake':
    if day_of_month <= 15:
        cake_price = 24
    elif day_of_month > 15:
        cake_price = 28.70
elif pastry == 'Souffle':
    if day_of_month <= 15:
        souffle_price = 6.66
    elif day_of_month > 15:
        souffle_price = 9.80
elif pastry == 'Baklava':
    if day_of_month <= 15:
        baklava_price = 12.60
    elif day_of_month > 15:
        baklava_price = 16.98

all_cake_price = cake_price * pastries_ordered
all_souffle_price = souffle_price * pastries_ordered
all_baklava_price = baklava_price * pastries_ordered
total_sum = all_cake_price + all_souffle_price + all_baklava_price

if day_of_month <= 22:
    if total_sum >= 100 and total_sum <= 200:
        discount = 0.15
    elif total_sum > 200:
        discount = 0.25

final_price = total_sum - (total_sum * discount)

if day_of_month <= 15:
    final_price = final_price * 0.90

print(f'{final_price:.2f}')