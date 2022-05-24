first_team_wins = 0
first_team_losses = 0
first_team_draws = 0

for game in range(3): # range(1, 3 + 1)
    current_result = input()
    first_team_result = int(current_result[0])
    second_team_result = int(current_result[2])

    if first_team_result > second_team_result:
        first_team_wins += 1
    elif second_team_result > first_team_result:
        first_team_losses += 1
    else: # first_team_results == second_team_results
        first_team_draws += 1

print(f'Team won {first_team_wins} games.')
print(f'Team lost {first_team_losses} games.')
print(f'Drawn games: {first_team_draws}')

# text = input()
#
# for character in text:
#     print(character)

# print(current_result)
# print(current_result[0])
# print(current_result[2])
# print(current_result[-1])
