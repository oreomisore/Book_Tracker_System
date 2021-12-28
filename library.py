from datetime import datetime


class Book:
    name: str = None
    author: str = None
    pages: int = None
    genre: str = None
    publisher: str = None
    date_published: int = None
    date_started: datetime = None
    date_finished: datetime = None

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_author(self) -> str:
        return self.author

    def set_author(self, author: str) -> None:
        self.author = author

    def get_pages(self) -> int:
        return self.pages

    def set_pages(self, pages: int) -> None:
        self.pages = pages

    def get_genre(self) -> str:
        return self.genre

    def set_genre(self, genre: str) -> None:
        self.genre = genre

    def get_publisher(self) -> str:
        return self.publisher

    def set_publisher(self, publisher: str) -> None:
        self.publisher = publisher

    def get_year_published(self) -> int:
        return self.date_published

    def set_year_published(self, date_published: int) -> None:
        self.date_published = date_published

    def get_date_started(self) -> datetime:
        return self.date_started

    def start(self):
        self.date_started = datetime.now()

    def finish(self):
        self.date_finished = datetime.now()

    def get_date_finished(self) -> datetime:
        return self.date_finished

    def display_information(self):
        print("Title: " + self.get_name())
        print("Author: " + self.get_author())
        print("Genre: {}".format(self.get_genre()))
        print("Pages: {}".format(self.get_pages()))
        print("Publisher: {}".format(self.get_publisher()))
        print("Publish Year: {}".format(self.get_year_published()))




class Library:
    book_list: [Book] = None

    def __init__(self, books: [Book] = None):
        self.book_list = []
        if books:
            self.book_list = books

    def add_book(self, book: Book):
        self.book_list.append(book)

    def remove_book(self, book_name: str):
        book = self.check_book(book_name)
        if book:
            self.book_list.remove(book)

    def check_book(self, book_str: str):
        for book in self.book_list:
            if book.name == book_str:
                # print("... Checking")
                # print(f"{book_str} is already in your library!")
                return book
        return None

    def clear_library(self):
        self.book_list.clear()

    def display_library(self):
        for items in self.book_list:
            print(items.name)

    def search_author(self, author: str):
        print("Books By {} : ".format(author))
        for items in self.book_list:
            if items.author == author:
                print(items.name)

    def search_genre(self, genre: str):
        print("{} Books in Library : ".format(genre))
        for books in self.book_list:
            for genre_items in books.genre:
                if genre_items == genre:
                    print(books.name)

    def book_count(self):
        book_quantity = len(self.book_list)
        print(" There are {} books in your library ...".format(book_quantity))

