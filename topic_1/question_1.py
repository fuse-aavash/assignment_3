class Book:
    def __init__(self, title: str, author: str, isbn: str, genre: str, availability: bool = True):
        """
        Represents a single book with attributes.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.
            isbn (str): ISBN (International Standard Book Number) of the book.
            genre (str): Genre of the book.
            availability (bool, optional): Whether the book is available for borrowing or not. Default is True.
        Attributes:
            title (str): Title of the book.
            author (str): Author of the book.
            isbn (str): ISBN (International Standard Book Number) of the book.
            genre (str): Genre of the book.
            availability (bool): Whether the book is available for borrowing or not.

        Examples:
            book = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Classic")
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.availability = availability

    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre}) - ISBN: {self.isbn}"


class LibraryCatalog:
    def __init__(self):
        """
        Manages the collection of books in the library catalog.

        Attributes:
            books (list): A list to store Book objects.

        Examples:
            catalog = LibraryCatalog()
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Add a book to the library catalog.

        Args:
            book (Book): The Book object to be added.

        Examples:
            book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Classic")
            catalog = LibraryCatalog()
            catalog.add_book(book1)
        """
        self.books.append(book)

    def get_book_details(self, title: str) -> Book:
        """
        Get the details of a book by title.

        Args:
            title (str): Title of the book to retrieve.

        Returns:
            Book: The Book object with the matching title.

        Raises:
            ValueError: If the book with the given title is not found in the catalog.

        Examples:
            catalog = LibraryCatalog()
            book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Classic")
            catalog.add_book(book1)
            book = catalog.get_book_details("The Great Gatsby")
            print(book)
        """
        for book in self.books:
            if book.title == title:
                return book
        raise ValueError(f"Book with title '{title}' not found in the catalog.")

    def get_all_books(self) -> list:
        """
        Get a list of all books in the library catalog.

        Returns:
            list: A list containing all the Book objects in the catalog.

        Examples:
            catalog = LibraryCatalog()
            book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Classic")
            book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", "Classic")
            catalog.add_book(book1)
            catalog.add_book(book2)
            all_books = catalog.get_all_books()
            for book in all_books:
                print(book)
        """
        return self.books

    def borrow_book(self, title: str):
        """
        Borrow a book by setting its availability to False.

        Args:
            title (str): Title of the book to borrow.

        Raises:
            ValueError: If the book with the given title is not found in the catalog or is already borrowed.

        Examples:
            catalog = LibraryCatalog()
            book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Classic")
            catalog.add_book(book1)

            # Borrow the book
            catalog.borrow_book("The Great Gatsby")

            # Try to borrow again (should raise ValueError)
            catalog.borrow_book("The Great Gatsby")
        """
        book = self.get_book_details(title)
        if not book.availability:
            raise ValueError(f"The book '{title}' is already borrowed.")
        book.availability = False
        print(f"The book '{title}' has been borrowed.")

    def return_book(self, title: str):
        """
        Return a book by setting its availability to True.

        Args:
            title (str): Title of the book to return.

        Raises:
            ValueError: If the book with the given title is not found in the catalog or is already available.

       
        """
        book = self.get_book_details(title)
        if book.availability:
            raise ValueError(f"The book '{title}' is already available.")
        book.availability = True
        print(f"The book '{title}' has been returned.")


# Test the classes
book1 = Book("Ghumne mech ma andho manche ", "Aavash Bhattarai", "978074327234", "Classic")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", "Classic")

catalog = LibraryCatalog()
catalog.add_book(book1)
catalog.add_book(book2)

# Get book details and print all books
book = catalog.get_book_details("The Great Gatsby")
print(book)

all_books = catalog.get_all_books()
for book in all_books:
    print(book)

# Borrow and return books
catalog.borrow_book("The Great Gatsby")
catalog.return_book("The Great Gatsby")