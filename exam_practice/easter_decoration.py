customer_count = int(input())

basket = 1.50
wreath = 3.80
bunny = 7
avg_bill = 0
bill = 0

for customer in range(1, customer_count + 1):

    bill = 0
    products_count = 0
    product_type = input()
    while product_type != 'Finish':
        purchased_product = product_type
        products_count += 1

        if purchased_product == 'basket':
            bill = bill + basket
        elif purchased_product == 'wreath':
            bill = bill + wreath
        elif purchased_product == 'chocolate bunny':
            bill = bill + bunny

        if product_type == 'Finish':
            break
        product_type = input()

    if products_count % 2 == 0:
        bill = bill * 0.80
        print(f"You purchased {products_count} items for {bill:.2f} leva.")
    else:
        print(f"You purchased {products_count} items for {bill:.2f} leva.")

    avg_bill = avg_bill + bill

print(f"Average bill per client is: {avg_bill / customer_count:.2f} leva.")
