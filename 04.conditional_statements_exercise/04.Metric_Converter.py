number = float(input())
input_margin = input()
output_margin = input()
if input_margin == 'mm':
    number /= 1000
elif input_margin == 'cm':
    number /= 100
if output_margin == 'mm':
    number *= 1000
elif output_margin == 'cm':
    number *= 100
print(f'{number:.3f}')