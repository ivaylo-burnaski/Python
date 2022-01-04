count_of_numbers = int(input())
count_of_symbols = int(input())
for symbol1 in range(1, count_of_numbers + 1):
    for symbol2 in range(1, count_of_numbers + 1):
        for symbol3 in range(97, 97 + count_of_symbols):
            for symbol4 in range(97, 97 + count_of_symbols):
                for symbol5 in range(1, count_of_numbers + 1):
                    if symbol5 > symbol1 and symbol5 > symbol2:
                        print(f'{symbol1}{symbol2}{chr(symbol3)}{chr(symbol4)}{symbol5}', end=' ')

