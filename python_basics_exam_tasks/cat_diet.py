fats_percent = int(input())
protein_percent = int(input())
carbs_percent = int(input())
all_calories = int(input())
water_percent = int(input())

fats_per_gram = 9 # kalorii
proteins_per_gram = 4 # kalorii
carbs_per_gram = 4 # kalorii

all_fats = (all_calories * (fats_percent / 100)) / fats_per_gram
all_proteins = (all_calories * protein_percent / 100) / proteins_per_gram
all_carbs = (all_calories * (carbs_percent / 100)) / carbs_per_gram

food_weight = all_carbs + all_proteins + all_fats
calories_per_gram = all_calories / food_weight

calories_without_water =  calories_per_gram * (water_percent / 100)

print(f'{(calories_per_gram - calories_without_water):.4f}')