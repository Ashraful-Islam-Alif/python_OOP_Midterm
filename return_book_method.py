class Book:
    def __init__(self, title, author, availability=True):
        self.title = title
        self.author = author
        self.availability = availability

    def borrow_book(self):
        if self.availability:
            self.availability = False
            print(f"The book '{self.title}' has been borrowed.")
        else:
            print(f"Sorry, the book '{self.title}' is currently unavailable.")

    def return_book(self):
        self.availability = True
        print(f"The book '{self.title}' has been returned and is now available.")
        
# Example usage:
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Borrowing the book
book1.borrow_book()

# Returning the book
book1.return_book()
