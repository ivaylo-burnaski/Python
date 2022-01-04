from math import floor
kind_of_year = input()
count_of_holidays = int(input())
count_of_weekends_he_travel = int(input())
yearly_weekends = 48
weekends_in_sofia = 48 - count_of_weekends_he_travel
sofia_plays = weekends_in_sofia * 3 / 4
home_plays = count_of_weekends_he_travel
holiday_plays = count_of_holidays * 2 / 3
total_plays = sofia_plays + home_plays + holiday_plays
if kind_of_year == 'leap':
    total_plays *= 1.15
print(f'{floor(total_plays)}')
