import math

current_record_in_seconds = float(input())
distance_in_meters = float(input())
meter_per_second = float(input())

distance_to_travel = distance_in_meters * meter_per_second
time_added = math.floor(distance_in_meters / 50) * 30
time_spent_climbing = time_added + distance_to_travel

diff = abs(current_record_in_seconds - time_spent_climbing)

if time_spent_climbing < current_record_in_seconds:
    print(f"Yes! The new record is {time_spent_climbing:.2f} seconds.")
else:
    print(f"No! He was {diff:.2f} seconds slower.")