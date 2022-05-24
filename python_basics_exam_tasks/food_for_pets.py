days = int(input())
food_count = float(input())

all_dog_eaten_food = 0
all_cat_eaten_food = 0
biscuits = 0

for i in range(1, days + 1):
    dog_eaten_food = float(input())
    cat_eaten_food = float(input())
    all_dog_eaten_food = all_dog_eaten_food + dog_eaten_food
    all_cat_eaten_food = all_cat_eaten_food + cat_eaten_food
    if i % 3 == 0:
        biscuits = (dog_eaten_food + cat_eaten_food) * 0.10


all_food_eaten = all_dog_eaten_food + all_cat_eaten_food
diff = food_count - (all_cat_eaten_food + all_dog_eaten_food)

percent_all_food_eaten = ((diff - food_count) / food_count) * 100
percent_of_dog_eaten_food = ((all_cat_eaten_food - all_food_eaten) / all_food_eaten) * 100
percent_of_cat_eaten_food = ((all_dog_eaten_food - all_food_eaten) / all_food_eaten) * 100

print(f'Total eaten biscuits: {biscuits}gr.')
print(f'{abs(percent_all_food_eaten):.2f}% of the food has been eaten.')
print(f"{abs(percent_of_dog_eaten_food):.2f}% eaten from the dog.")
print(f"{abs(percent_of_cat_eaten_food):.2f}% eaten from the cat.")