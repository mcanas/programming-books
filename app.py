import csv
import datetime
from models import Base, Book, engine, session


# main menu - add, search, view all, analysis, exit
def menu():
    while True:
        print('''
            \nPROGRAMMING BOOKS
            \r1) Add a New Book
            \r2) View All Books
            \r3) Search for a Book
            \r4) Book Analysis
            \r5) Exit
        ''')
        choice = input('What would you like to do? ')
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            input('''
                \rPlease choose one of the options above.
                \rA number from 1-5.
                \rPress enter to try again.
            ''')


# add books to database
def add_book(title, author, date_published, price):
    book_in_db = session.query(Book).filter(Book.title == title).one_or_none()
    if book_in_db == None:
        new_book = Book(title=title, author=author,
                        date_published=date_published, price=price)
        session.add(new_book)
        session.commit()
        print('Book added!')


# View all books
def view_all_books():
    books = session.query(Book).all()
    for book in books:
        print(book)


# edit books
def edit_book():
    pass


# delete books
def delete_book():
    pass


# search books
def search_book(id):
    pass


# data import
def import_books(filepath):
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=(
            'title', 'author', 'date_published', 'price'))
        rows = list(reader)
        for row in rows:
            add_book(**clean_row(row))


# data cleaning
def clean_date(date):
    try:
        cleaned_date = datetime.datetime.strptime(date, '%B %d, %Y').date()
    except ValueError:
        print(
            'The value entered is not the correct format. Please enter a date in the format: January 1, 2021')
    else:
        return cleaned_date
    return None


def clean_price(price):
    try:
        cleaned_price = int(float(price) * 100)
    except ValueError:
        print(
            'The value entered is not the correct format. Please enter a price in the format: 19.95')
    else:
        return cleaned_price
    return None


def clean_row(fields):
    fields['date_published'] = clean_date(fields['date_published'])
    fields['price'] = clean_price(fields['price'])
    return fields


# app loop
def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            # add book
            title = input('Title: ')
            author = input('Author: ')

            while True:
                date = input('Published Date (Ex: January 1, 2021): ')
                date = clean_date(date)
                if type(date) == datetime.date:
                    break

            while True:
                price = input('Price (Ex: 19.95): ')
                price = clean_price(price)
                if type(price) == int:
                    break

            add_book(title, author, date, price)
            pass
        elif choice == '2':
            view_all_books()
            # view books
            pass
        elif choice == '3':
            # search for books
            pass
        elif choice == '4':
            # book analysis
            pass
        else:
            print('Goodbye!')
            app_running = False


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    import_books('suggested_books.csv')
    app()
