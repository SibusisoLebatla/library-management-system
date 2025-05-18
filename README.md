# 📚 Assignment 14-  Peer Review, Onboarding,
and Open-Source Collaboration
## 🚀 Getting Started
This project was prepared for open-source collaboration as part of Assignment 14. The following enhancements were completed:

✅ **CONTRIBUTING.md** – Provides setup, coding standards, and how to submit PRs  
✅ **Labeled Issues** – 
- `good-first-issue` (5+ beginner-friendly tasks)  
- `feature-request` (3+ ideas for improvement)  
✅ **ROADMAP.md** – Future features like Redis caching, pagination, and authentication  
✅ **README.md** – Improved with setup, CI/CD, contribution guide, feature table  
✅ **LICENSE** – Open-source license added (MIT)  
✅ **Peer Sharing** – Repository shared with classmates for stars/forks and feedback  
✅ **Reflection** – Written reflection in `REFLECTION.md` about the collaboration experience  
✅ **VOTING_RESULTS.md** – Will track GitHub stars and forks from classmates


### Clone and Install
git clone https://github.com/SibusisoLebatla/library-management-system

# 📚 Assignment 13- Implementing CI/CD with
GitHub Actions
## ✅ CI/CD Pipeline (GitHub Actions)

### 💡 How it Works
- **Triggers on**: Every push and PR to `main`
- **Runs**: Unit tests and integration tests
- **Blocks**: Merges to `main` if tests fail
- **Builds**: Artifact on successful merge to `main`

### 🔧 Running Tests Locally




# 📚 Assignment 12 – Service-Oriented Library API

This project is a layered, testable, RESTful system for managing books in a library. It includes a domain model, in-memory repository, service layer, REST API, unit tests, integration tests, and OpenAPI documentation.

---

## ✅ Architecture Overview

### 1. **Domain Model**
- Defined in `/src/book.py`
- Represents a Book with ID, title, and checkout state.

### 2. **Repository Layer**
- Generic interface in `/repositories/base_repository.py`
- Specific interface for books: `/repositories/book_repository.py`
- In-memory implementation: `/repositories/inmemory/in_memory_book_repository.py`
- Placeholder for future database: `/repositories/database/database_book_repository.py`

### 3. **Factory Pattern**
- `/factories/repository_factory.py` selects the appropriate repository based on config.

### 4. **Service Layer**
- `/services/book_service.py` contains business logic like checkout, create, update.
- Includes exceptions like `BookNotFoundException`.

### 5. **API Layer** (Next Step)
- RESTful endpoints using FastAPI (upcoming).
- Sample endpoints:
  - `GET /api/books` - list all books
  - `POST /api/books` - create new book
  - `PUT /api/books/{id}` - update book
  - `POST /api/books/{id}/checkout` - check out book

### 6. **Testing**
- Unit tests in `/tests/`
  - Repository: `test_in_memory_book_repository.py`
  - Services: `tests/services/test_book_service.py`
- Integration API tests: `/tests/api/test_book_api.py` (next)

### 7. **Documentation**
- Mermaid class diagram in `/docs/class_diagram.md`
- Swagger UI auto-generated via FastAPI at `/docs`
- Optional OpenAPI export in `/docs/openapi_schema.json`

---

## ✅ Setup Instructions

### 📦 Requirements
- Python 3.10+
- FastAPI
- pytest

### 🔧 Run Unit Tests

```bash
pytest tests/





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
