from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from services.book_service import BookService
from factories.repository_factory import RepositoryFactory
from src.book import Book

# Request/response schemas
class BookRequest(BaseModel):
    book_id: str
    title: str

class BookUpdateRequest(BaseModel):
    title: str

# Instantiate service with in-memory repository
book_service = BookService(RepositoryFactory.get_book_repository("MEMORY"))

router = APIRouter(prefix="/api/books", tags=["Books"])

@router.get("/", response_model=List[Book])
def get_all_books():
    return book_service.get_all_books()

@router.post("/", response_model=Book)
def create_book(book: BookRequest):
    return book_service.create_book(book.book_id, book.title)

@router.put("/{book_id}", response_model=Book)
def update_book(book_id: str, request: BookUpdateRequest):
    try:
        return book_service.update_book(book_id, request.title)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/{book_id}/checkout", response_model=Book)
def checkout_book(book_id: str):
    try:
        return book_service.checkout_book(book_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
