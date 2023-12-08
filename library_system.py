class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}"

    def borrow(self):
        if self.available:
            self.available = False
        else:
            print("This book is currently not available.")

    def return_book(self):
        self.available = True


class Patron:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print("This book is currently not available.")

    def return_book(self, book):
        book.return_book()
        self.borrowed_books.remove(book)

    def display_borrowed_books(self):
        return [book.display_info() for book in self.borrowed_books]

# Create two books
book1 = Book('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565')
book2 = Book('To Kill a Mockingbird', 'Harper Lee', '9780446310789')

# Display their information
print(book1.display_info())
print(book2.display_info())

# Check availability (should be True)
print(f"Is '{book1.title}' available? {book1.available}")
print(f"Is '{book2.title}' available? {book2.available}")

# Create a patron
patron = Patron('John Doe', '123')

# Patron tries to borrow the books
patron.borrow_book(book1)
patron.borrow_book(book2)

# Check availability again (should be False)
print(f"Is '{book1.title}' available? {book1.available}")
print(f"Is '{book2.title}' available? {book2.available}")

# Display the books currently borrowed by the patron (should be both books)
print("Books currently borrowed by John Doe:")
for book in patron.display_borrowed_books():
    print(book)

# Patron returns the first book
patron.return_book(book1)

# Check availability again (should be True for the first book and False for the second)
print(f"Is '{book1.title}' available? {book1.available}")
print(f"Is '{book2.title}' available? {book2.available}")

# Display the books currently borrowed by the patron (should be only the second book)
print("Books currently borrowed by John Doe:")
for book in patron.display_borrowed_books():
    print(book)
