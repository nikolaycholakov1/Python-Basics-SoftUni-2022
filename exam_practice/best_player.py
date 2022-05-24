current_player = input()

best_player = ''
current_goals = 0

while current_player != 'END':
    current_player_goals = int(input())

    if current_player_goals > current_goals:
        current_goals = current_player_goals
        best_player = current_player

    if current_player_goals >= 10:
        break

    current_player = input()

if current_goals < 3:
    print(f"{best_player} is the best player!")
    print(f"He has scored {current_goals} goals.")
else:
    print(f"{best_player} is the best player!")
    print(f"He has scored {current_goals} goals and made a hat-trick !!!")