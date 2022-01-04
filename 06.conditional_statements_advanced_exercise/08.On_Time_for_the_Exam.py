hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())
time_of_exam = hour_of_exam * 60 + minute_of_exam
time_of_arrival = hour_of_arrival * 60 + minute_of_arrival
if time_of_exam < time_of_arrival:
    print('Late')
    if time_of_arrival - time_of_exam < 60:
        print(f'{time_of_arrival - time_of_exam} minutes after the start')
    else:
        hour_late = (time_of_arrival - time_of_exam) // 60
        minute_late = (time_of_arrival - time_of_exam) % 60
        if minute_late <= 9:
            print(f'{hour_late}:0{minute_late} hours after the start')
        else:
            print(f'{hour_late}:{minute_late} hours after the start')
elif 0 <= time_of_exam - time_of_arrival <= 30:
    print('On time')
    if time_of_exam - time_of_arrival != 0:
        print(f'{time_of_exam - time_of_arrival} minutes before the start')
elif 30 < time_of_exam - time_of_arrival < 60:
    print('Early')
    print(f'{time_of_exam - time_of_arrival} minutes before the start')
elif time_of_exam - time_of_arrival >= 60:
    print('Early')
    hour_early = (time_of_exam - time_of_arrival) // 60
    minute_early = (time_of_exam - time_of_arrival) % 60
    if minute_early <= 9:
        print(f'{hour_early}:0{minute_early} hours before the start')
    else:
        print(f'{hour_early}:{minute_early} hours before the start')
