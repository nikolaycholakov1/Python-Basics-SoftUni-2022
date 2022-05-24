peak = 8848
meters_climbed = 5364
days_climbing = 1

will_rest_or_end = input()
while will_rest_or_end != 'END':
    meters_to_climb = int(input())

    if will_rest_or_end == 'Yes':
        days_climbing += 1

    meters_climbed += meters_to_climb

    if meters_climbed >= peak or days_climbing == 5:
        break

    will_rest_or_end = input()

if meters_climbed < peak:
    print('Failed!')
    print(f'{meters_climbed}')
elif meters_climbed >= peak:
    print(f"Goal reached for {days_climbing} days!")
