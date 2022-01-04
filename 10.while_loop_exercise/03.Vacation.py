needed_money = float(input())
saved_money = float(input())
spend_counter = 0
passed_days = 0
money_are_spend = False
while saved_money < needed_money:
    action = input()
    money = float(input())
    passed_days += 1
    if action == 'save':
        saved_money += money
        spend_counter = 0
    elif action == 'spend':
        spend_counter += 1
        saved_money -= money
        if saved_money < 0:
            saved_money = 0
        if spend_counter == 5:
            money_are_spend = True
            break
if money_are_spend:
    print("You can't save the money.")
    print(f'{passed_days}')
else:
    print(f'You saved the money for {passed_days} days.')
