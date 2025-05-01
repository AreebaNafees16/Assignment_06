class Book:
    total_books = 0  # Class variable to keep track of total books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Increment count when a new book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Increment the class variable

    @classmethod
    def get_total_books(cls):
        return cls.total_books  # Return the total number of books


# Example usage
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Accessing total_books using the class method
print("Total books in the collection:", Book.get_total_books())
