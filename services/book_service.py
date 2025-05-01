from repositories.book_repository import BookRepository
from src.book import Book

class BookNotFoundException(Exception):
    pass

class BookAlreadyCheckedOutException(Exception):
    pass

class BookService:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    def checkout_book(self, book_id: str) -> Book:
        book = self.book_repo.find_by_id(book_id)
        if not book:
            raise BookNotFoundException(f"Book '{book_id}' not found")

        if book.checked_out:
            raise BookAlreadyCheckedOutException(f"Book '{book_id}' is already checked out")

        book.check_out()
        self.book_repo.save(book)
        return book

    def get_all_books(self) -> list[Book]:
        return self.book_repo.find_all()

    def create_book(self, book: Book) -> Book:
        self.book_repo.save(book)
        return book

    def update_book(self, book_id: str, title: str) -> Book:
        book = self.book_repo.find_by_id(book_id)
        if not book:
            raise BookNotFoundException(f"Book '{book_id}' not found")

        book.title = title
        self.book_repo.save(book)
        return book
