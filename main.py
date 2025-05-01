from fastapi import FastAPI
from api.book_api import router as book_router

app = FastAPI(
    title="Library API",
    version="1.0.0",
    description="API for managing books and checkouts"
)

app.include_router(book_router)
