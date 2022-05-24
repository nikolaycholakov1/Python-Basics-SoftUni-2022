locations_count = int(input())

for location in range(1, locations_count + 1):
    daily_gold_needed = float(input())
    days_to_dig = int(input())

    location_average = 0
    excavated_gold = 0
    days_digging = 0
    diff = 0

    gold_per_day = float(input())
    while True:
        days_digging += 1
        excavated_gold += gold_per_day

        if days_digging == days_to_dig:
            location_average = excavated_gold / days_to_dig
            if location_average >= daily_gold_needed:
                print(f"Good job! Average gold per day: {location_average:.2f}.")
            else:
                diff = abs(daily_gold_needed - location_average)
                print(f"You need {diff:.2f} gold.")
            break

        gold_per_day = float(input())