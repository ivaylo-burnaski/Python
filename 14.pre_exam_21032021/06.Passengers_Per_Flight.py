from math import floor
from sys import maxsize
airline_count = int(input())
count_of_flights = 0
total_passengers = 0
max_average_passengers_count = -maxsize
max_average_passengers_count_company_name = ''
for airline in range(airline_count):
    airline_name = input()
    line = input()
    count_of_flights = 0
    total_passengers = 0
    while line != 'Finish':
        count_passengers_per_flight = int(line)
        count_of_flights += 1
        total_passengers += count_passengers_per_flight
        line = input()
    average_count_of_passengers = floor(total_passengers / count_of_flights)
    print(f'{airline_name}: {average_count_of_passengers} passengers.')
    if average_count_of_passengers > max_average_passengers_count:
        max_average_passengers_count = average_count_of_passengers
        max_average_passengers_count_company_name = airline_name
print(f'{max_average_passengers_count_company_name} has most passengers per flight: {max_average_passengers_count}')
