import pytest
from src.book import Book
from services.book_service import BookService, BookNotFoundException, BookAlreadyCheckedOutException
from repositories.inmemory.in_memory_book_repository import InMemoryBookRepository

def test_checkout_book_success():
    repo = InMemoryBookRepository()
    book = Book("B1", "Clean Architecture")
    repo.save(book)

    service = BookService(repo)
    checked_out = service.checkout_book("B1")

    assert checked_out.checked_out is True

def test_checkout_book_not_found():
    service = BookService(InMemoryBookRepository())
    with pytest.raises(BookNotFoundException):
        service.checkout_book("X123")

def test_checkout_book_already_checked_out():
    repo = InMemoryBookRepository()
    book = Book("B2", "Domain-Driven Design")
    book.check_out()
    repo.save(book)

    service = BookService(repo)
    with pytest.raises(BookAlreadyCheckedOutException):
        service.checkout_book("B2")
