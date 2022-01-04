world_record = float(input())
distance = float(input())
speed = float(input())
swimmer_time = distance * speed
delay = distance // 15 * 12.5
swimmer_time += delay
if swimmer_time < world_record:
    print(f'Yes, he succeeded! The new world record is {swimmer_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {swimmer_time - world_record:.2f} seconds slower.')
