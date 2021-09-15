import csv
from datetime import datetime
from models import Base, Book, engine, session

MAIN_MENU = '''\nPROGRAMMING BOOKS
1) Add a New Book
2) View All Books
3) Search for a Book
4) Book Analysis
5) Exit
'''


# main menu - add, search, view all, analysis, exit
def menu(choice=0):
    if choice == 0:
        print(MAIN_MENU)
        choice = int(input(f'\nWhat would you like to do? '))
        return menu(choice)
    elif choice == 1:
        print('Add a New Book')
        title = input('Title: ')
        author = input('Author: ')
        date_published = input('Date published: ')
        price = input('Price: ')
        # add_book(title, author, date_published, price)
        print('Book added!')
    elif choice == 5:
        print('exit!')
        return False
    return True


# add books to database
def add_book(title, author, date_published, price):
    new_book = Book(title=title, author=author,
                    date_published=date_published, price=price)
    session.add(new_book)
    session.commit()


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
def clean_row(fields):
    fields['date_published'] = datetime.strptime(
        fields['date_published'], '%B %d, %Y').date()
    fields['price'] = float(fields['price'])
    return fields


# app loop
def start():
    Base.metadata.create_all(engine)
    while menu():
        continue


if __name__ == '__main__':
    start()
