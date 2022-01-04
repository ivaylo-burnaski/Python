line = input()
total = 0
while line != 'NoMoreMoney':
    income = float(line)
    if income < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {income:.2f}')
    total += income
    line = input()
print(f'Total: {total:.2f}')
