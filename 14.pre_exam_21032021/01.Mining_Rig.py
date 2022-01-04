from math import ceil
video_card_price = int(input())
adapter_price = int(input())
electricity_price_for_day_per_card = float(input())
income_for_day_per_card = float(input())
cards_price = video_card_price * 13
adapters_price = adapter_price * 13
spent_money = cards_price + adapters_price + 1000
income_for_day_per_card -= electricity_price_for_day_per_card
income_from_cards_per_day = 13 * income_for_day_per_card
days_to_regain_money = ceil(spent_money / income_from_cards_per_day)
print(spent_money)
print(days_to_regain_money)
