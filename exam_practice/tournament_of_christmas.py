days = int(input())

wins = 0
losses = 0
win_counter = 0
loss_counter = 0
daily_winnings = 0
tournament_won = False


for i in range(1, days + 1):
    input_line = input()

    while input_line != 'Finish':
        sport = (input_line)
        win_or_lose = input()

        if win_or_lose == 'win':
            win_counter += 1
        elif win_or_lose == 'lose':
            loss_counter += 1

        daily_winnings = win_counter * 20

        if win_counter > loss_counter:
            daily_winnings = daily_winnings * 1.10
            tournament_won = True

        input_line = input()

if tournament_won:
    daily_winnings = daily_winnings * 1.20
    print(f"You won the tournament! Total raised money: {daily_winnings:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {daily_winnings:.2f}")