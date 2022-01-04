line = input()
kids_counter = 0
adult_counter = 0
toys_price = 0
sweaters_price = 0
while line != 'Christmas':
    family_member_age = int(line)
    if family_member_age <= 16:
        kids_counter += 1
    else:
        adult_counter += 1
    line = input()
toys_price = kids_counter * 5
sweaters_price = adult_counter * 15
print(f'Number of adults: {adult_counter}')
print(f'Number of kids: {kids_counter}')
print(f'Money for toys: {toys_price}')
print(f'Money for sweaters: {sweaters_price}')
