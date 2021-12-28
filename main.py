import datetime

from library import Book, Library

RUN_TIMER = 84600


class LibEngine:
    run_time = RUN_TIMER
    selected_book = None
    input = None
    start_time = None
    read_books_lib: Library = None
    currently_reading_lib: Library = None
    unread_book_lib: Library = None
    books_dict = None
    books_dict_name = None
    genre_dict = None


    def __init__(self):
        self.start_time = datetime.datetime.now()
        self.read_books_lib = Library()
        self.currently_reading_lib = Library()
        self.unread_book_lib = Library()
        self.books_dict = {}
        self.genre_dict = {}
        self.books_dict_name = {}
        #self.start()

    def start(self):
        while int((datetime.datetime.now() - self.start_time).seconds) < RUN_TIMER:
            var = input("Please Type menu to see options /  Press number associated with option : ")
            var = var.strip().lower()

            if var == "menu":
                print("Enter values 1 - 8:")
                print("1. Add a book to a library \n"
                      "2. View all Books in a Library \n"
                      "3. Clear a Library \n"
                      "4. Find a book \n"
                      "5. Display all books \n"
                      "6. Display book information \n"
                      "7. Display books with the same genre \n"
                      "8. Quit \n"
                      ">")


            if var == "1":
                var2 = input("Press 'n' to add a new book or Press 'a' to add an existing book")
                var2 = var2.strip().lower()
                if var2 == 'n':
                    name = input("Enter the name of the book: ")
                    author = input("Enter the author of the book: ")
                    genres = input("Enter the genre of the book: ")
                    # TODO pages = int(input("Enter the number of pages of the book: "))
                    new_book = Book()
                    new_book.set_name(name)
                    new_book.set_author(author)
                    new_book.set_genre(genres)
                    self.selected_book = new_book
                if var2 == 'a':
                    self.list_all_books()
                    for key in self.books_dict_name.keys():
                        print(f"{key} : {self.books_dict_name[key]} \n ")
                    book_number = input("Select the number of the book you would like to add? :")
                    library = input("Enter the library you would like to add this book to:"
                                    "1. Unread books "
                                    "2. Currently-Reading "
                                    "3. Finished Books"
                                    ">")

                    if library == '1':
                        book = self.books_dict[book_number][0]
                        lib = self.books_dict[book_number][1]
                        if lib == 'u':
                            print("Book already in Unread library ")
                            continue
                        else:
                            self.unread_book_lib.add_book(book)
                            if lib == "r":
                                self.read_books_lib.remove_book(book.name)
                            if lib == 'c':
                                self.currently_reading_lib.remove_book(book.name)

                    elif library == '2':
                        book = self.books_dict[book_number][0]
                        lib = self.books_dict[book_number][1]
                        if lib == 'c':
                            print("Book already in currently-reading library ")
                            continue
                        else:
                            self.currently_reading_lib.add_book(book)
                            if lib == 'u':
                                self.unread_book_lib.remove_book(book.name)
                            if lib == 'r':
                                self.read_books_lib.remove_book(book.name)


                    elif library == '3':
                        book = self.books_dict[book_number][0]
                        lib = self.books_dict[book_number][1]
                        if lib == 'r':
                            print("Book already in Finished Books library ")
                            continue
                        else:
                            self.read_books_lib.add_book(book)
                            if lib == 'u':
                                self.unread_book_lib.remove_book(book.name)
                            if lib == 'c':
                                self.currently_reading_lib.remove_book(book.name)

                    #TODO ERRORS

            if var == '2':
                book_library = input("Select the library you would like to view: \n"
                                     "1. Unread books \n"
                                     "2. Currently-Reading \n"
                                     "3. Finished books \n"
                                     ">")

                if book_library == '1':
                    self.unread_book_lib.display_library()
                elif book_library == '2':
                    self.currently_reading_lib.display_library()
                elif book_library == '3':
                    self.read_books_lib.display_library()
                else:
                    print("\nWhat you have entered is not a valid number, try again.")

            if var == '3':
                book_library = input("Select the library you would like to clear: \n"
                                     "1. Unread books \n"
                                     "2. Currently-Reading \n"
                                     "3. Finished books \n"
                                     ">")

                if book_library == '1':
                    self.unread_book_lib.clear_library()
                    print("Unread books Library cleared...")
                elif book_library == '2':
                    self.currently_reading_lib.clear_library()
                    print("Currently-Read Library cleared...")
                elif book_library == '3':
                    self.read_books_lib.clear_library()
                    print("Finished books Library cleared...")
                else:
                    print("\nWhat you have entered is not a valid number, try again.")

            if var == '4':
                self.list_all_books()
                for key in self.books_dict_name.keys():
                    print(f"{key} : {self.books_dict_name[key]} \n ")
                book_number = input("Select the number of the book you would like to find :")
                book = self.books_dict[book_number][0]
                lib = self.books_dict[book_number][1]
                if lib == "r":
                    print(f"{book.name} in Finished Library")
                if lib == "u":
                    print(f"{book.name} in Unread Library")
                if lib == "c":
                    print(f"{book.name} in Currently-Reading Library")

            if var == "5":
                self.list_all_books()
                print("*" * 40)
                for key in self.books_dict_name.keys():
                    print(f"{key} : {self.books_dict_name[key]} \n ")


            if var == "6":
                self.list_all_books()
                for key in self.books_dict_name.keys():
                    print(f"{key} : {self.books_dict_name[key]} \n ")
                book_number = input("Select the number of the book you would like to view :")
                book = self.books_dict[book_number][0]
                print("*" * 40)
                print(f"About {book.name}: ")
                print("*" * 40)
                book.display_information()


            if var == '7':
                self.list_all_books()
                self.list_all_genre()
                genre_number = int(input("Select the number of the genre would you like to search for from the above ?"))
                for keys in self.genre_dict.keys():
                    if genre_number == keys:
                        print("*" * 40)
                        print(f"{self.genre_dict[keys]} books in your library:")
                        print("*" * 40)
                        for items in self.books_dict.values():
                            book = items[0]
                            if book.genre == self.genre_dict[keys]:
                                print(book.name)


            if var == '8':
                print("Sad to see you leave :(")
                return


    def list_all_books(self):
        i = 0
        for book in self.read_books_lib.book_list:
            i += 1
            self.books_dict[str(i)] = [book, 'r']
            self.books_dict_name[str(i)] = book.name
        for book in self.unread_book_lib.book_list:
            i += 1
            self.books_dict[str(i)] = [book, 'u']
            self.books_dict_name[str(i)] = book.name
        for book in self.currently_reading_lib.book_list:
            i += 1
            self.books_dict[str(i)] = [book, 'c']
            self.books_dict_name[str(i)] = book.name

    def list_all_genre(self):
        i = 0
        list1 = [book.genre for book in self.read_books_lib.book_list]
        list2 = [book.genre for book in self.currently_reading_lib.book_list]
        list3 = [book.genre for book in self.unread_book_lib.book_list]
        set1 = set(list1 + list2 + list3)
        for item in set1:
            i += 1
            self.genre_dict[i] = item
            print(f"{i} : {item}")



if __name__ == '__main__':
    eng = LibEngine()
    book1 = Book()
    book1.set_name("Handmaids Tale")
    book1.set_author('Margaret Atwood')
    book1.set_genre('Dystopian novel')
    book1.set_pages(311)
    book1.set_publisher('Houghton Mifflin Company')
    book1.set_year_published(1985)
    #book1.display_information()
    eng.unread_book_lib.add_book(book1)

    book2 = Book()
    book2.set_name('Malibu Rising')
    book2.set_author('Taylor Jenkins Reid')
    book2.set_genre('Historical Fiction')
    book2.set_pages(384)
    eng.unread_book_lib.add_book(book2)

    book3 = Book()
    book3.set_name('The Seven Husbands of Evelyn Hugo')
    book3.set_author('Taylor Jenkins Reid')
    book3.set_genre('Romance')
    book3.set_pages(400)
    eng.unread_book_lib.add_book(book3)

    book4 = Book()
    book4.set_name('Daisy Jones and The Six')
    book4.set_author('Taylor Jenkins Reid')
    book4.set_genre('Historical Fiction')
    book4.set_pages(400)
    eng.unread_book_lib.add_book(book4)

    book5 = Book()
    book5.set_name('Fall of Giants')
    book5.set_author('Ken Follett')
    book5.set_genre('Historical Fiction')
    book5.set_pages(1008)
    eng.unread_book_lib.add_book(book5)


    book6 = Book()
    book6.set_name('Winter of the World')
    book6.set_author('Ken Follett')
    book6.set_genre('Historical Fiction')
    book6.set_pages(940)
    eng.unread_book_lib.add_book(book6)

    book7 = Book()
    book7.set_name('Edge of Eternity')
    book7.set_author('Ken Follett')
    book7.set_genre('Historical Fiction')
    book7.set_pages(1184)
    eng.unread_book_lib.add_book(book7)

    #eng.unread_book_lib.display_library()
    eng.start()


