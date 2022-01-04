strawberries_price = float(input())
bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberries = float(input())
raspberries_price = strawberries_price / 2
oranges_price = 0.6 * raspberries_price
bananas_price = 0.2 * raspberries_price
bill = bananas * bananas_price + oranges * oranges_price + raspberries * raspberries_price + strawberries * strawberries_price
print(bill)