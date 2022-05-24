budget = float(input())

products_sum = 0
purchase_counter = 0
remaining_money = budget

command = input()
while command != 'Stop':
    product_type = command
    product_price = float(input())
    purchase_counter += 1

    if purchase_counter % 3 == 0:
        product_price = product_price * 0.50

    products_sum = products_sum + product_price
    remaining_money -= product_price
    if remaining_money - product_price < 0:
        break

    command = input()

if budget < products_sum:
    print("You don't have enough money!")
    print(f"You need {abs(remaining_money):.2f} leva!")
elif budget > products_sum:
    print(f"You bought {purchase_counter} products for {products_sum:.2f} leva.")
