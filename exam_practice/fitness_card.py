our_money = float(input())
gender = (input())
age = int(input())
sport = (input())

tax = 0
discount = 0

if sport == 'Gym':
    if gender == 'm':
        tax = 42
    elif gender == 'f':
        tax = 35
elif sport == 'Boxing':
    if gender == 'm':
        tax = 41
    elif gender == 'f':
        tax = 37
elif sport == 'Yoga':
    if gender == 'm':
        tax = 45
    elif gender == 'f':
        tax = 42
elif sport == 'Zumba':
    if gender == 'm':
        tax = 34
    elif gender == 'f':
        tax = 31
elif sport == 'Dances':
    if gender == 'm':
        tax = 51
    elif gender == 'f':
        tax = 53
elif sport == 'Pilates':
    if gender == 'm':
        tax = 39
    elif gender == 'f':
        tax = 37

if age <= 19:
    discount = 0.80
    tax = tax * discount

diff = abs(our_money - tax)

if our_money > tax:
    print(f"You purchased a 1 month pass for {sport}.")
elif our_money < tax:
    print(f"You don't have enough money! You need ${diff:.2f} more.")