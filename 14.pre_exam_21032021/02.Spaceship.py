from math import floor
spaceship_width = float(input())
spaceship_length = float(input())
spaceship_height = float(input())
astronauts_average_height = float(input())
spaceship_volume = spaceship_length * spaceship_width * spaceship_height
room_volume = (astronauts_average_height + 0.4) * 2 * 2
free_astronaut_spaces = floor(spaceship_volume / room_volume)
if free_astronaut_spaces < 3:
    print('The spacecraft is too small.')
elif free_astronaut_spaces > 10:
    print('The spacecraft is too big.')
else:
    print(f'The spacecraft holds {free_astronaut_spaces} astronauts.')
