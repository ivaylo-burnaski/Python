steps_counter = 0
goal_is_reached = False
line = input()
while line != 'Going home':
    steps = int(line)
    steps_counter += steps
    if steps_counter >= 10000:
        goal_is_reached = True
        break
    line = input()
if steps_counter < 10000:
    line = input()
    steps = int(line)
    steps_counter += steps
    if steps_counter >= 10000:
        goal_is_reached = True
if goal_is_reached:
    print('Goal reached! Good job!')
    print(f'{steps_counter - 10000} steps over the goal!')
else:
    print(f'{10000 - steps_counter} more steps to reach goal.')
