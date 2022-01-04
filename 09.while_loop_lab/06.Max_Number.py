import sys
max_number = -sys.maxsize
line = input()
while line != 'Stop':
    number = int(line)
    if number > max_number:
        max_number = number
    line = input()
print(max_number)
