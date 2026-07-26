class Library:
    def __init__(self):
        #variables
        self.no_of_books = 0
        self.books = []

    #add a book
    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1
        print(f'"{book_name}" added in library.')

    # get all books
    def show_books(self):
        if self.no_of_books == 0:
            print("Library is empty.")
        else:
            print("\nBooks in Library:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")

    #total books
    def get_no_of_books(self):
        return self.no_of_books


#creating object of Library class
lib = Library()

#adding book
lib.add_book("Python Basics")
lib.add_book("DBMS")
lib.add_book("c++")
lib.add_book("Machine Learning")

#show library
lib.show_books()

#number of books
print("Total number of books:", lib.get_no_of_books())

print("\n--- Program Ended ---")
print("If you run the program again, books will not be saved.\n")