trip_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())
income = puzzles_count * 2.6 + dolls_count * 3 + teddy_bears_count * 4.1 + minions_count * 8.2 + trucks_count * 2
toys_count = puzzles_count + dolls_count + teddy_bears_count + minions_count + trucks_count
if toys_count >= 50:
    income *= 0.75
income *= 0.9
if income >= trip_price:
    print(f"Yes! {income - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {abs(income - trip_price):.2f} lv needed.")