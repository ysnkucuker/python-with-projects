import sqlite3
import time


class Book:
    def __init__(self, title, author, publisher, genre, edition):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.edition = edition

    def __str__(self):
        return (
            f"Title : {self.title}\n"
            f"Author : {self.author}\n"
            f"Publisher : {self.publisher}\n"
            f"Genre : {self.genre}\n"
            f"Edition : {self.edition}"
        )


class Library:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = sqlite3.connect("library.db")
        self.cursor = self.connection.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS books (
            title TEXT,
            author TEXT,
            publisher TEXT,
            genre TEXT,
            edition INTEGER
        )
        """
        self.cursor.execute(query)
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

    def show_books(self):
        query = "SELECT * FROM books"
        self.cursor.execute(query)
        books = self.cursor.fetchall()

        if len(books) == 0:
            print("No books found in the library.")
        else:
            for b in books:
                book = Book(b[0], b[1], b[2], b[3], b[4])
                print(book)
                print("-" * 30)

    def search_book(self, title):
        query = "SELECT * FROM books WHERE title = ?"
        self.cursor.execute(query, (title,))
        books = self.cursor.fetchall()

        if len(books) == 0:
            print("Book not found.")
        else:
            book = Book(*books[0])
            print("Book found:")
            print(book)

    def add_book(self, book):
        query = "INSERT INTO books VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(
            query,
            (book.title, book.author, book.publisher, book.genre, book.edition),
        )
        self.connection.commit()

    def delete_book(self, title):
        query = "DELETE FROM books WHERE title = ?"
        self.cursor.execute(query, (title,))
        self.connection.commit()

    def increase_edition(self, title):
        query = "SELECT * FROM books WHERE title = ?"
        self.cursor.execute(query, (title,))
        books = self.cursor.fetchall()

        if len(books) == 0:
            print("Book not found.")
        else:
            edition = books[0][4] + 1
            update_query = "UPDATE books SET edition = ? WHERE title = ?"
            self.cursor.execute(update_query, (edition, title))
            self.connection.commit()
