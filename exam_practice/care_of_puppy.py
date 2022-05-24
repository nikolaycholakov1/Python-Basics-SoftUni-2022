food_in_kg = int(input())

input_line = input()

available_food = food_in_kg * 1000
food_eaten = 0

while input_line != 'Adopted':
    daily_food = int(input_line)
    food_eaten = (food_eaten + daily_food)

    input_line = input()

diff = abs(available_food - food_eaten)

if available_food >= food_eaten:
    print(f"Food is enough! Leftovers: {diff} grams." )
else:
    print(f"Food is not enough. You need {diff} grams more." )