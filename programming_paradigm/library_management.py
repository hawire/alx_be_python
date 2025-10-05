
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        """Mark the book as available again."""
        if self._is_checked_out:
            self._is_checked_out = False
        else:
            print(f"'{self.title}' was not checked out.")

    def is_available(self):
        """Return True if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a new book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in library.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book titled '{title}' not found in library.")

    def list_available_books(self):
        """List all books that are available."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
