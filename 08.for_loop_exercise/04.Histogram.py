n = int(input())
count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0
for i in range(1, n + 1):
    number = int(input())
    if number < 200:
        count_p1 += 1
    elif 200 <= number <= 399:
        count_p2 += 1
    elif 400 <= number <= 599:
        count_p3 += 1
    elif 600 <= number <= 799:
        count_p4 += 1
    elif number >= 800:
        count_p5 += 1
print(f'{count_p1 / n * 100:.2f}%')
print(f'{count_p2 / n * 100:.2f}%')
print(f'{count_p3 / n * 100:.2f}%')
print(f'{count_p4 / n * 100:.2f}%')
print(f'{count_p5 / n * 100:.2f}%')
