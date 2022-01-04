n = int(input())
washing_machine_price = float(input())
toy_price = int(input())
count_of_toys = 0
collected_money = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        collected_money += i * 5 - 1
    else:
        count_of_toys += 1
total_sum = count_of_toys * toy_price + collected_money
if total_sum >= washing_machine_price:
    print(f'Yes! {total_sum - washing_machine_price:.2f}')
else:
    print(f'No! {washing_machine_price - total_sum:.2f}')
