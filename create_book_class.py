class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

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
    # Creating book objects
    book1 = Book(1, "The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", False)

    # Adding books to the library
    Library.entry_book(book1)
    Library.entry_book(book2)

    # Viewing all books in the library
    print("Current books in the library:", Library.book_list)
