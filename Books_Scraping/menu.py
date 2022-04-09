from app import books




USER_CHOICE = ''' Enter one of the following

- 'b' to look for 5-star books
- 'c' to look for the cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to exit

Enter your choice: 
'''


def print_best_books():
    best_books = sorted(books, key = lambda x: x.rating * -1)[:5]
    for book in best_books:
        print(book)




def print_chepeast_books():
    chepeast_books = sorted(books, key = lambda x: x.price)[:5]
    for book in chepeast_books:
        print(book)

books_generator = (x for x in books)
def get_next_book():
    print(next(books_generator))

def len_of_books():
    print(len(books))


user_choices = {
    'a': len_of_books,
    'b': print_best_books,
    'c': print_chepeast_books,
    'n': get_next_book
}



def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n', 'a'):
            user_choices[user_input]()
        else:
            print("please select a valid choice!!")

        user_input = input(USER_CHOICE)

menu()






