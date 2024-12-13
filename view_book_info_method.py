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

# Example usage
if __name__ == "__main__":
    # Creating book objects (automatically adds them to the library)
    book1 = Book(1, "The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", False)

    # Borrowing and returning books
    book1.borrow_book()  # Should mark the book as borrowed
    book1.return_book()  # Should mark the book as available

    # Viewing book information
    book1.view_book_info()
    book2.view_book_info()

    # Viewing all books in the library
    print("Current books in the library:", Library.book_list)
