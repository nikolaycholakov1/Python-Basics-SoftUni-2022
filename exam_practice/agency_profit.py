airline = input()
adult_tickets = int(input())
kid_tickets = int(input())
adult_ticket_price = float(input())
service_tax = float(input())

kid_ticket_price = adult_ticket_price * 0.30 + service_tax
actual_adult_ticket_price = adult_ticket_price + service_tax

profit = (kid_ticket_price * kid_tickets) + (actual_adult_ticket_price * adult_tickets)
diff = profit * 0.20

print(f'The profit of your agency from {airline} tickets is {diff:.2f} lv.')