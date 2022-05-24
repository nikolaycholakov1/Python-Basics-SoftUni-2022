min_per_day = int(input())
daily_walks = int(input())
daily_calories = int(input())

all_minutes_walking = min_per_day * daily_walks
burned_calories = all_minutes_walking * 5

if daily_calories / 2 > burned_calories:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")
else:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")