name_of_film = input()
kind_of_hall = input()
purchased_tickets = int(input())
ticket_price = 0
if name_of_film == 'A Star Is Born':
    if kind_of_hall == 'normal':
        ticket_price = 7.5
    elif kind_of_hall == 'luxury':
        ticket_price = 10.5
    elif kind_of_hall == 'ultra luxury':
        ticket_price = 13.5
elif name_of_film == 'Bohemian Rhapsody':
    if kind_of_hall == 'normal':
        ticket_price = 7.35
    elif kind_of_hall == 'luxury':
        ticket_price = 9.45
    elif kind_of_hall == 'ultra luxury':
        ticket_price = 12.75
elif name_of_film == 'Green Book':
    if kind_of_hall == 'normal':
        ticket_price = 8.15
    elif kind_of_hall == 'luxury':
        ticket_price = 10.25
    elif kind_of_hall == 'ultra luxury':
        ticket_price = 13.25
elif name_of_film == 'The Favourite':
    if kind_of_hall == 'normal':
        ticket_price = 8.75
    elif kind_of_hall == 'luxury':
        ticket_price = 11.55
    elif kind_of_hall == 'ultra luxury':
        ticket_price = 13.95
income = ticket_price * purchased_tickets
print(f'{name_of_film} -> {income:.2f} lv.')