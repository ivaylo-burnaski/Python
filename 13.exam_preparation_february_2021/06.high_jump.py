target_height = int(input())
lath_height = target_height - 30
count_of_bad_jumps = 0
count_of_all_jumps = 0
is_Failed = False
while lath_height <= target_height:
    for jump in range(1, 4):
        count_of_all_jumps += 1
        jumped_height = int(input())
        if jumped_height > lath_height:
            lath_height += 5
            count_of_bad_jumps = 0
            break
        else:
            count_of_bad_jumps += 1
            if count_of_bad_jumps == 3:
                is_Failed = True
                break
    if is_Failed:
        break
if is_Failed:
    print(f'Tihomir failed at {lath_height}cm after {count_of_all_jumps} jumps.')
else:
    print(f'Tihomir succeeded, he jumped over {target_height}cm after {count_of_all_jumps} jumps.')
