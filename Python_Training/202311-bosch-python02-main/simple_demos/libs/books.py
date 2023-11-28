class Book:
    pass

def create_book(title,author,price,rating):
    book=Book()
    book.title = title
    book.author = author
    book.price = price
    book.rating = rating
    return book

def print_books(books, caption=None):
    print(caption.center(93))
    print()
    print('-'*93)
    print(f'| {"Title".center(25)} | {"Author".center(25)} | {"Price".center(15)} | {"Rating".center(15)} |')
    print('-'*93)

    for book in books:
        print(f'| {book.title.center(25)} | {book.author.center(25)} | {str(book.price).rjust(13)}   | {str(book.rating).rjust(13)}   |')

    print('-'*93)
    print()


def get_books():
    return [
        create_book('The Acccursed God','Vivek Dutta Mishra',299,4.6),
        create_book('Rashmirathi','Ramdhari Singh Dinkar',109,4.8),
        create_book('Asura','Neelkanthan',499,3.6),
        create_book('Manas','Vivek Dutta Mishra',199,4.5),
        create_book('One Night at Call Center','Chetan Bhagat',399,3.9),
        create_book('Kuruksehtra','Ramdhari Singh Dinkar',99,4.1),
    ]


if __name__=='__main__':
    books=get_books()
    print_books(books,'Original List')