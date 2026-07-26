class Library:
    def __init__(self):
        self.books = []

    # Add a book
    def add_book(self, book_name):

        if book_name in self.books:
            print(f'"{book_name}" already exists in the library.')
        else:
            self.books.append(book_name)
            print(f'"{book_name}" added successfully.')

    # Show all books
    def show_books(self):

        if len(self.books) == 0:
            print("\nLibrary is empty.")
        else:
            print("\n------ Books in Library ------")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")

    # Total number of books
    def total_books(self):

        print(f"\nTotal Books: {len(self.books)}")

    # Search book
    def search_book(self, book_name):

        if book_name in self.books:
            print(f'"{book_name}" is available.')
        else:
            print(f'"{book_name}" is NOT available.')

    # Remove book
    def remove_book(self, book_name):

        if book_name in self.books:
            self.books.remove(book_name)
            print(f'"{book_name}" removed successfully.')
        else:
            print(f'"{book_name}" not found.')


# ~~~ MAIN PROGRAM ~~~

lib = Library()

while True:
    print("\n====== LIBRARY MENU ======")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Total Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        lib.add_book(book)

    elif choice == "2":
        lib.show_books()

    elif choice == "3":
        book = input("Enter book name to search: ")
        lib.search_book(book)

    elif choice == "4":
        book = input("Enter book name to remove: ")
        lib.remove_book(book)

    elif choice == "5":
        lib.total_books()

    elif choice == "6":
        print("\nThank you for using the Library Management System.")
        break

    else:
        print("Invalid choice! Please try again.")