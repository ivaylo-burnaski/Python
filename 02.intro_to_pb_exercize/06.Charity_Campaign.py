days_of_campaign = int(input())
sheff_count = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())
total_sum = ((cakes * 45) + (waffles * 5.8) + (pancakes * 3.2)) * sheff_count * days_of_campaign
total_sum -= total_sum / 8
print(total_sum)
