from repositories.inmemory.in_memory_book_repository import InMemoryBookRepository
from src.book import Book

def test_save_and_find():
    repo = InMemoryBookRepository()
    book = Book("B1", "Design Patterns")
    repo.save(book)
    found = repo.find_by_id("B1")
    assert found.title == "Design Patterns"

def test_delete():
    repo = InMemoryBookRepository()
    book = Book("B2", "Clean Code")
    repo.save(book)
    repo.delete("B2")
    assert repo.find_by_id("B2") is None

def test_find_all():
    repo = InMemoryBookRepository()
    book1 = Book("B3", "Book A")
    book2 = Book("B4", "Book B")
    repo.save(book1)
    repo.save(book2)
    all_books = repo.find_all()
    assert len(all_books) == 2
