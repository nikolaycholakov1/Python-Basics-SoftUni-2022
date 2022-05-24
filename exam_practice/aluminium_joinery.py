joinery_count = int(input())
joinery_size = input()
delivery_type = input()

price = 0
discount = 0
second_discount = 0.96
final_price = 0

if joinery_size == '90X130':
    price = 110
    if 30 > joinery_count <= 60:
        discount = 0.95
    elif joinery_count > 60:
        discount = 0.92
elif joinery_size == '100X150':
    price = 140
    if 40 > joinery_count <= 80:
        discount = 0.94
    elif joinery_count > 80:
        discount = 0.90
elif joinery_size == '130X180':
    price = 190
    if 20 > joinery_count <= 50:
        discount = 0.93
    elif joinery_count > 50:
        discount = 0.88
elif joinery_size == '200X300':
    price = 250
    if 25 > joinery_count <= 50:
        discount = 0.91
    elif joinery_count > 50:
        discount = 0.86

if delivery_type == 'With delivery':
    final_price = 60 + ((price * joinery_count) * discount)
elif delivery_type == 'Without delivery':
    final_price = (price * joinery_count) * discount

if joinery_count <= 10:
    print('Invalid order')
elif joinery_count < 99:
    print(f'{final_price:.2f} BGN')
elif joinery_count > 100:
    print(f'{second_discount * final_price:.2f} BGN')