destination = input()
saved_money = 0
while destination != 'End':
    min_needed_money = float(input())
    while saved_money < min_needed_money:
        income = float(input())
        saved_money += income
    print(f'Going to {destination}!')
    saved_money = 0
    destination = input()
