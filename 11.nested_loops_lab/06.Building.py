floors_count = int(input())
rooms_count = int(input())
for f in range(floors_count, 0, -1):
    for r in range(0, rooms_count):
        if f == floors_count:
            print(f'L{f}{r}', end=' ')
        elif f % 2 == 0:
            print(f'O{f}{r}', end=' ')
        else:
            print(f'A{f}{r}', end=' ')
    print()
