from math import ceil
height_of_wall = int(input())
width_of_wall = int(input())
percent_not_to_paint = int(input())
total_paint_area = height_of_wall * width_of_wall * 4
area_to_paint = ceil(total_paint_area * (100 - percent_not_to_paint) / 100)
needed_litres = area_to_paint
spent_litres = 0
is_painted = False
line = input()
while line != 'Tired!':
    litres_of_paint = int(line)
    spent_litres += litres_of_paint
    if spent_litres >= needed_litres:
        is_painted = True
        break
    line = input()
if is_painted:
    paint_left = spent_litres - needed_litres
    if paint_left == 0:
        print('All walls are painted! Great job, Pesho!')
    else:
        print(f'All walls are painted and you have {paint_left} l paint left!')
else:
    meters_to_paint = needed_litres - spent_litres
    print(f'{meters_to_paint} quadratic m left.')
