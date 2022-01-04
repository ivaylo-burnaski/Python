city = input()
sells = float(input())
commission = 0
if city == 'Sofia':
    if 0 <= sells <= 500:
        commission = 0.05 * sells
    elif 500 < sells <= 1000:
        commission = 0.07 * sells
    elif 1000 < sells <= 10000:
        commission = 0.08 * sells
    elif sells > 10000:
        commission = 0.12 * sells
    else:
        print('error')
elif city == 'Varna':
    if 0 <= sells <= 500:
        commission = 0.045 * sells
    elif 500 < sells <= 1000:
        commission = 0.075 * sells
    elif 1000 < sells <= 10000:
        commission = 0.10 * sells
    elif sells > 10000:
        commission = 0.13 * sells
    else:
        print('error')
elif city == 'Plovdiv':
    if 0 <= sells <= 500:
        commission = 0.055 * sells
    elif 500 < sells <= 1000:
        commission = 0.08 * sells
    elif 1000 < sells <= 10000:
        commission = 0.12 * sells
    elif sells > 10000:
        commission = 0.145 * sells
    else:
        print('error')
else:
    print('error')
if commission != 0:
    print(f'{commission:.2f}')
