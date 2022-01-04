change = float(input())
change_in_coins = int(change * 100)
coins_counter = 0
while change_in_coins != 0:
    if change_in_coins // 200 > 0:
        coins_counter += 1
        change_in_coins -= 200
    elif change_in_coins // 100 > 0:
        coins_counter += 1
        change_in_coins -= 100
    elif change_in_coins // 50 > 0:
        coins_counter += 1
        change_in_coins -= 50
    elif change_in_coins // 20 > 0:
        coins_counter += 1
        change_in_coins -= 20
    elif change_in_coins // 10 > 0:
        coins_counter += 1
        change_in_coins -= 10
    elif change_in_coins // 5 > 0:
        coins_counter += 1
        change_in_coins -= 5
    elif change_in_coins // 2 > 0:
        coins_counter += 1
        change_in_coins -= 2
    elif change_in_coins == 0:
        break
    else:
        coins_counter += 1
        change_in_coins -= 1
print(coins_counter)
