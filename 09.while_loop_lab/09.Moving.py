width = int(input())
length = int(input())
height = int(input())
place = width * length * height
line = input()
total_packs = 0
while line != 'Done':
    count_of_packs = int(line)
    total_packs += count_of_packs
    if total_packs > place:
        break
    line = input()
if place >= total_packs:
    print(f'{place - total_packs} Cubic meters left.')
else:
    print(f'No more free space! You need {total_packs - place} Cubic meters more.')
