class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability
        # Automatically add the book to the Library book_list
        Library.entry_book(self)

    def borrow_book(self):
        if self.availability:
            self.availability = False
            print(f"You have successfully borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is currently not available.")

    def return_book(self):
        if not self.availability:
            self.availability = True
            print(f"You have successfully returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")

    def view_book_info(self):
        availability_status = "Available" if self.availability else "Not Available"
        print(f"Book ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}\nAvailability: {availability_status}")

    def __repr__(self):
        return (f"Book(book_id={self.book_id}, title='{self.title}', "
                f"author='{self.author}', availability={self.availability})")

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
                    book.borrow_book()
                else:
                    print("Book not found.")
            elif choice == 3:
                book_id = int(input("Enter the Book ID to return: "))
                book = next((b for b in Library.book_list if b.book_id == book_id), None)
                if book:
                    book.return_book()
                else:
                    print("Book not found.")
            elif choice == 4:
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
