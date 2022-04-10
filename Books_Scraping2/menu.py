from app import books

USER_CHOICES = '''

-'b': get best books
-'c': get cheapest books
-'n': get the next book
-'q': quit the program

'''



book_generator = (book for book in books)
def get_next_book():
    
    print(next(book_generator))

def get_best_books():
    sorted_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in sorted_books:
        print(book)

def get_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)

def total_books():
    print(len(books))

user_choices = {
    'b': get_best_books,
    'c': get_cheapest_books,
    'n': get_next_book,
    'm': total_books
}

def menu():
    user_input = input(USER_CHOICES)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n', 'm'):
            user_choices[user_input]()
        else:
            print("invlaid!! select a valid choice")
        user_input = input(USER_CHOICES)

menu()