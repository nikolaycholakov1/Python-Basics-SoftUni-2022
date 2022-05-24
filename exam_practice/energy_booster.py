fruit = input()
set_size = input()
count_of_boosters = int(input())

sets = 0
booster_price = 0
discount = 0

if fruit == 'Watermelon':
    if set_size == 'small':
        sets = 2
        booster_price = sets * count_of_boosters * 56
    elif set_size == 'big':
        sets = 5
        booster_price = sets * count_of_boosters * 28.70
elif fruit == 'Mango':
    if set_size == 'small':
        sets = 2
        booster_price = sets * count_of_boosters * 36.66
    elif set_size == 'big':
        sets = 5
        booster_price = sets * count_of_boosters * 19.60
elif fruit == 'Pineapple':
    if set_size == 'small':
        sets = 2
        booster_price = sets * count_of_boosters * 42.10
    elif set_size == 'big':
        sets = 5
        booster_price = sets * count_of_boosters * 24.80
elif fruit == 'Raspberry':
    if set_size == 'small':
        sets = 2
        booster_price = sets * count_of_boosters * 20
    elif set_size == 'big':
        sets = 5
        booster_price = sets * count_of_boosters * 15.20

if booster_price < 400:
    booster_price = booster_price
elif booster_price <= 1000:
    discount = 0.85
    booster_price = booster_price * discount
elif booster_price > 1000:
    discount = 0.50
    booster_price = booster_price * discount

print(f'{booster_price:.2f} lv.')