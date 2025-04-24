from repositories.book_repository import BookRepository
from src.book import Book

class DatabaseBookRepository(BookRepository):
    def save(self, book: Book) -> None:
        raise NotImplementedError("Database storage not implemented yet")

    def find_by_id(self, book_id: str):
        raise NotImplementedError("Database storage not implemented yet")

    def delete(self, book_id: str):
        raise NotImplementedError("Database storage not implemented yet")

    def find_all(self):
        raise NotImplementedError("Database storage not implemented yet")
