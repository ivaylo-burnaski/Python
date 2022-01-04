a1 = int(input())
a2 = int(input())
n = int(input())
for i in range(a1, a2):
    if i % 2 == 0:
        continue
    s1 = chr(i)
    s4 = i
    for j in range(1, n):
        s2 = j
        n1 = int(n / 2)
        for k in range(1, n1):
            s3 = k
            if (s2 + s3 + s4) % 2 != 0:
                print(f'{s1}-{s2}{s3}{s4}')
