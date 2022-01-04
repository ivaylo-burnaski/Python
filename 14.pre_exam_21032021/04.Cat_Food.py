cats_count = int(input())
count_small_cats = 0
count_big_cats = 0
count_huge_cats = 0
total_food = 0
for cat in range(cats_count):
    grams_food = float(input())
    total_food += grams_food
    if 100 <= grams_food < 200:
        count_small_cats += 1
    elif 200 <= grams_food < 300:
        count_big_cats += 1
    elif 300 <= grams_food < 400:
        count_huge_cats += 1
print(f'Group 1: {count_small_cats} cats.')
print(f'Group 2: {count_big_cats} cats.')
print(f'Group 3: {count_huge_cats} cats.')
food_price = total_food / 1000 * 12.45
print(f'Price for food per day: {food_price:.2f} lv.')
