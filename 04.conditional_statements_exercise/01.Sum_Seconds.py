racer1_time = int(input())
racer2_time = int(input())
racer3_time = int(input())
total_time = racer1_time + racer2_time + racer3_time
minutes = total_time // 60
seconds = total_time % 60
if seconds <= 9:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')