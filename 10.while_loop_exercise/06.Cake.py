width = int(input())
length = int(input())
is_finished = False
count_of_pieces = width * length
line = input()
while line != 'STOP':
    taken_pieces = int(line)
    count_of_pieces -= taken_pieces
    if count_of_pieces <= 0:
       is_finished = True
       break
    line = input()
if is_finished:
    print(f'No more cake left! You need {abs(count_of_pieces)} pieces more.')
else:
    print(f'{count_of_pieces} pieces are left.')