from repositories.base_repository import Repository
from src.book import Book

class BookRepository(Repository[Book, str]):
    pass
