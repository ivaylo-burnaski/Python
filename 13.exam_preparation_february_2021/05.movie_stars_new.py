budget = float(input())
line = input()
while line != 'ACTION':
    actor_name = line
    if len(actor_name) > 15:
        actor_payment = 0.2 * budget
    else:
        actor_payment = float(input())
    budget -= actor_payment
    if budget <= 0:
        break
    line = input()
if budget > 0:
    print(f'We are left with {budget:.2f} leva.')
else:
    print(f'We need {abs(budget):.2f} leva for our actors.')