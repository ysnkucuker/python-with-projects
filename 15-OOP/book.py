class Book:
    def __init__(self, title, author, page_count, genre):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.genre = genre

    def __str__(self):
        return f"""
Title  : {self.title}
Author : {self.author}
Pages  : {self.page_count}
Genre  : {self.genre}
"""

    def __len__(self):
        return self.page_count

    def __del__(self):
        print("Book object is being deleted...")
