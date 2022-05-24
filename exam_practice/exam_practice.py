btc = int(input())
chinese_uan = float(input())
commission = float(input())

commission_percentage = "{:.0f}%".format(commission)

btc_to_lv = btc * 1168
chinese_uan_to_dollar = chinese_uan * 0.15
dollars_to_lv = chinese_uan_to_dollar * 1.76
leva = btc_to_lv + dollars_to_lv

euro = leva / 1.95
commission_percent = euro - commission_percentage

final_sum = euro - commission_percent
print(commission_percentage)
print(f'{final_sum:.2f}')
