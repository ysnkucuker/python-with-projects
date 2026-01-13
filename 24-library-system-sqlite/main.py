import time
from library import *

print("""
************************** Welcome to the Library Management System **************************

Operations:
1. Show All Books
2. Search Book
3. Add Book
4. Delete Book
5. Increase Book Edition

Press 'q' to quit.
""")

library = Library()

while True:
    operation = input("Select an operation: ")

    if operation == "q":
        print("Exiting program...")
        break

    elif operation == "1":
        library.show_books()

    elif operation == "2":
        title = input("Enter book title: ")
        print("Searching book...")
        time.sleep(2)
        library.search_book(title)

    elif operation == "3":
        title = input("Title: ")
        author = input("Author: ")
        publisher = input("Publisher: ")
        genre = input("Genre: ")
        edition = int(input("Edition: "))

        new_book = Book(title, author, publisher, genre, edition)
        print("Adding book...")
        time.sleep(2)
        library.add_book(new_book)

    elif operation == "4":
        title = input("Enter the title of the book to delete: ")
        confirm = input("Are you sure? [Y/N]: ")

        if confirm.lower() == "y":
            print("Deleting book...")
            time.sleep(2)
            library.delete_book(title)
            print("Book deleted.")

    elif operation == "5":
        title = input("Enter the book title to increase edition: ")
        print("Updating edition...")
        time.sleep(2)
        library.increase_edition(title)

    else:
        print("Invalid operation.")
