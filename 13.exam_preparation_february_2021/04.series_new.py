budget = float(input())
serial_count = int(input())
spent_money = 0
for serial in range (1, serial_count + 1):
    serial_name = input()
    price_for_serial = float(input())
    if serial_name == 'Thrones':
        price_for_serial *= 0.5
    elif serial_name == 'Lucifer':
        price_for_serial *= 0.6
    elif serial_name == 'Protector':
        price_for_serial *= 0.7
    elif serial_name == 'TotalDrama':
        price_for_serial *= 0.8
    elif serial_name == 'Area':
        price_for_serial *= 0.9
    spent_money += price_for_serial
if spent_money > budget:
    print(f'You need {spent_money - budget:.2f} lv. more to buy the series!')
else:
    print(f'You bought all the series and left with {budget - spent_money:.2f} lv.')