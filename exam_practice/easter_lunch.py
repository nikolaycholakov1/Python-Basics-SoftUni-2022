number_of_cakes = int(input())
eggs = int(input())
number_of_cookies = int(input())

number_of_all_eggs = eggs * 12
total_sum = 0
total_sum += number_of_cakes * 3.20
total_sum += eggs * 4.35
total_sum += number_of_cookies * 5.40
total_sum += number_of_all_eggs * 0.15

print(f'{total_sum:.2f}')