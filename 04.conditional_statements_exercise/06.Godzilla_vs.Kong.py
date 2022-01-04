movie_budget = float(input())
stats_count = int(input())
stats_suite_price = float(input())
decoration = movie_budget * 0.1
total_suite_price = stats_count * stats_suite_price
if stats_count > 150:
    total_suite_price *= 0.9
total_cost = decoration + total_suite_price
if total_cost > movie_budget:
    print('Not enough money!')
    print(f'Wingard needs {total_cost - movie_budget:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {movie_budget - total_cost:.2f} leva left.')