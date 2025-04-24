# 📘 Assignment 11 – Repository Pattern & Persistence Abstraction
This assignment builds on top of Assignment 10 by introducing a Repository Layer to cleanly separate persistence logic from business logic. The solution uses the Repository Pattern, an in-memory implementation, a factory-based abstraction, and is structured to allow future extension with other storage backends (e.g., database, file system).

## ✅ What's Implemented
📁 /repositories/ – Repository Interfaces
base_repository.py: A generic interface using TypeVar and Generic from typing. Avoids duplication of CRUD logic across entities.

book_repository.py: An entity-specific repository interface for Book, extending the generic base.

✨ Used generics to avoid duplication across entity repositories.

## 🧠 /repositories/inmemory/ – In-Memory Implementations
in_memory_book_repository.py: Implements BookRepository using a Python dictionary (HashMap style). Supports:

save()

find_by_id()

delete()

find_all()

✅ This implementation is useful for fast unit testing and local experimentation.

## 🏭 /factories/ – Factory Pattern Abstraction
repository_factory.py: Chooses the appropriate repository based on storage type (e.g., "MEMORY" or "DATABASE"). This makes the codebase loosely coupled and highly swappable.

🔧 Used the Factory Pattern for simplicity and easy plug-in of new storage mechanisms.

## 🔮 /repositories/database/ – Future-Proof Stub
database_book_repository.py: Stub implementation of a repository that will one day connect to a real database.

🧩 This shows how we plan to extend our system with additional storage backends.

## 🧪 /tests/ – Unit Tests for In-Memory Repo
test_in_memory_book_repository.py:

Tests saving, finding, deleting, and listing books using InMemoryBookRepository.

⚡ Ensures correctness and helps support test-driven development.
















# Assignment 10 – Creational Design Patterns in Library System

## 💻 Language: Python
I chose Python for its simplicity, readability, and support for rapid prototyping of design patterns.

## 🧠 Patterns Used

| Pattern | Purpose | File |
|--------|---------|------|
| Simple Factory | Centralized item creation | `simple_factory.py` |
| Factory Method | Interface + subclasses for Payment | `factory_method.py` |
| Abstract Factory | Multiple UI components (buttons) | `abstract_factory.py` |
| Builder | Step-by-step pizza creation | `builder.py` |
| Prototype | Clone book objects | `prototype.py` |
| Singleton | One database connection | `singleton.py` |

## 📁 Project Structure

```bash
/src               # Domain classes
/creational_patterns   # All 6 creational patterns
/tests             # Unit tests for each pattern
README.md
CHANGELOG.md
