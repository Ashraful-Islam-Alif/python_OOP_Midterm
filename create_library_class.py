class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

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
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

    # Adding books to the library
    Library.entry_book(book1)
    Library.entry_book(book2)

    # Viewing all books in the library
    print("Current books in the library:", Library.book_list)
