from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_book():
    response = client.post("/api/books", json={"book_id": "B1", "title": "Test Book"})
    assert response.status_code == 200
    assert response.json()["book_id"] == "B1"

def test_get_books():
    client.post("/api/books", json={"book_id": "B2", "title": "Another Book"})
    response = client.get("/api/books")
    assert response.status_code == 200
    assert len(response.json()) >= 1

def test_update_book():
    client.post("/api/books", json={"book_id": "B3", "title": "Old Title"})
    response = client.put("/api/books/B3", json={"title": "New Title"})
    assert response.status_code == 200
    assert response.json()["title"] == "New Title"

def test_checkout_book():
    client.post("/api/books", json={"book_id": "B4", "title": "Checkout Me"})
    response = client.post("/api/books/B4/checkout")
    assert response.status_code == 200
    assert response.json()["is_checked_out"] is True
