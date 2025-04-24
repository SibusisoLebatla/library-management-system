from repositories.inmemory.in_memory_book_repository import InMemoryBookRepository
#from repositories.database.database_book_repository import DatabaseBookRepository (stub)

class RepositoryFactory:
    @staticmethod
    def get_book_repository(storage_type: str):
        if storage_type == "MEMORY":
            return InMemoryBookRepository()
        elif storage_type == "DATABASE":
            raise NotImplementedError("DatabaseBookRepository not implemented yet")
        else:
            raise ValueError("Invalid storage type")
