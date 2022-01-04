name_of_film = input()
student_count = 0
standard_count = 0
kid_count = 0
total_tickets = 0
while name_of_film != 'Finish':
    free_places = int(input())
    ticket_type = input()
    taken_places = 0
    while ticket_type != 'End':
        if ticket_type == 'student':
            student_count += 1
        elif ticket_type == 'standard':
            standard_count += 1
        elif ticket_type == 'kid':
            kid_count += 1
        taken_places += 1
        total_tickets += 1
        if taken_places == free_places:
            break
        ticket_type = input()
    percent = taken_places / free_places * 100
    print(f'{name_of_film} - {percent:.2f}% full.')
    name_of_film = input()
print(f'Total tickets: {total_tickets}')
percent_student_tickets = student_count / total_tickets * 100
print(f'{percent_student_tickets:.2f}% student tickets.')
percent_standard_tickets = standard_count / total_tickets * 100
print(f'{percent_standard_tickets:.2f}% standard tickets.')
percent_kid_tickets = kid_count / total_tickets * 100
print(f'{percent_kid_tickets:.2f}% kids tickets.')
