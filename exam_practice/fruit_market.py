strawberry_price_per_kg = float(input())
banana_count = float(input())
orange_count = float(input())
malini_count = float(input())
strawberry_count = float(input())

malini_price_per_kg = strawberry_price_per_kg * 0.50
orange_price_per_kg = malini_price_per_kg * 0.60
banana_price_per_kg = malini_price_per_kg - (malini_price_per_kg * 0.80)

bill_for_strawberry = strawberry_count * strawberry_price_per_kg
bill_for_malini = malini_count * malini_price_per_kg
bill_for_orange = orange_count * orange_price_per_kg
bill_for_banana = banana_count * banana_price_per_kg

total_sum = bill_for_banana + bill_for_orange + bill_for_malini + bill_for_strawberry

print(f'{total_sum:.2f}')