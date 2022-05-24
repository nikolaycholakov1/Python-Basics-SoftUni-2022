import math

ball_count = int(input())

all_points = 0
points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_colors = 0

for ball in range(1, ball_count + 1):
    ball_color = input()

    if ball_color == 'red' or ball_color == 'orange' or ball_color == 'yellow' \
            or ball_color == 'white' or ball_color == 'black':
        if ball_color == 'red':
            red_balls += 1
            points = points + 5
        elif ball_color == 'orange':
            orange_balls += 1
            points = points + 10
        elif ball_color == 'yellow':
            yellow_balls += 1
            points = points + 15
        elif ball_color == 'white':
            white_balls += 1
            points = points + 20
        elif ball_color == 'black':
            black_balls += 1
            points = math.floor(points / 2)
    else:
        other_colors += 1

print(f"Total points: {points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_colors}")
print(f"Divides from black balls: {black_balls}")
