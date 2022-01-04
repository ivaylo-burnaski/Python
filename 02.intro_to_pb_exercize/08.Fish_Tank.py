length = int(input())
width = int(input())
height = int(input())
percentage_occupied_volume = float(input())
volume = length * width * height * 0.001
volume -= volume * percentage_occupied_volume / 100
print(volume)
