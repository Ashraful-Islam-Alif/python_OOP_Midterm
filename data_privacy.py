class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id  # Private attribute
        self.__title = title      # Private attribute
        self.__author = author    # Private attribute
        self.__availability = availability  # Private attribute
        # Automatically add the book to the Library book_list
        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"You have successfully borrowed '{self.__title}'.")
        else:
            raise Exception(f"The book '{self.__title}' is already borrowed.")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"You have successfully returned '{self.__title}'.")
        else:
            raise Exception(f"The book '{self.__title}' was not borrowed.")

    def view_book_info(self):
        availability_status = "Available" if self.__availability else "Not Available"
        print(f"Book ID: {self.__book_id}\nTitle: {self.__title}\nAuthor: {self.__author}\nAvailability: {availability_status}")

    def __repr__(self):
        return (f"Book(book_id={self.__book_id}, title='{self.__title}', "
                f"author='{self.__author}', availability={self.__availability})")

    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def availability(self):
        return self.__availability

class Library:
    book_list = []  # Class attribute to store books

    @classmethod
    def entry_book(cls, book):
        if isinstance(book, Book):
            cls.book_list.append(book)
            print(f"Book '{book.title}' by {book.author} added to the library.")
        else:
            raise TypeError("Only objects of class 'Book' can be added to the library.")

    @classmethod
    def view_all_books(cls):
        if cls.book_list:
            for book in cls.book_list:
                book.view_book_info()
                print("-" * 30)
        else:
            print("No books are available in the library.")

# Example usage
if __name__ == "__main__":
    # Creating book objects (automatically adds them to the library)
    book1 = Book(1, "The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", False)

    while True:
        print("\nLibrary Menu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                Library.view_all_books()
            elif choice == 2:
                book_id = int(input("Enter the Book ID to borrow: "))
                book = next((b for b in Library.book_list if b.book_id == book_id), None)
                if book:
                    try:
                        book.borrow_book()
                    except Exception as e:
                        print(e)
                else:
                    print("Invalid Book ID. Please try again.")
            elif choice == 3:
                book_id = int(input("Enter the Book ID to return: "))
                book = next((b for b in Library.book_list if b.book_id == book_id), None)
                if book:
                    try:
                        book.return_book()
                    except Exception as e:
                        print(e)
                else:
                    print("Invalid Book ID. Please try again.")
            elif choice == 4:
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
