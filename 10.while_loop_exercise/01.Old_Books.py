favourite_book = input()
book_counter = 0
book_is_found = False
line = input()
while line != 'No More Books':
    if line == favourite_book:
        book_is_found = True
        break
    book_counter += 1
    line = input()
if book_is_found:
    print(f'You checked {book_counter} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {book_counter} books.')