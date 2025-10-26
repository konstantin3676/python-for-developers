from functools import wraps
from typing import List, Optional
from pydantic import BaseModel, EmailStr, field_validator

class Book(BaseModel):
    title: str
    author: str
    year: int
    available: bool = True
    categories: List[str] = []

    @field_validator('categories')
    @classmethod
    def categories_must_not_be_empty_strings(cls, v: List[str]) -> List[str]:
        if any(not cat.strip() for cat in v):
            raise ValueError('Категории не должны содержать пустые строки')
        return v

class User(BaseModel):
    name: str
    email: EmailStr
    membership_id: str

class BookNotAvailable(Exception):
    pass

books_db: List[Book] = []
users_db: List[User] = []

def add_book(book: Book) -> None:
    books_db.append(book)

def find_book(title: str) -> Optional[Book]:
    for book in books_db:
        if book.title == title:
            return book
    return None

def is_book_borrow(title: str) -> None:
    book = find_book(title)
    if book is None:
        raise ValueError(f"Книга '{title}' не найдена.")
    if not book.available:
        raise BookNotAvailable(f"Книга '{title}' недоступна для выдачи.")
    book.available = False

def return_book(title: str) -> None:
    book = find_book(title)
    if book is None:
        raise ValueError(f"Книга '{title}' не найдена.")
    book.available = True

class Library(BaseModel):
    books: List[Book] = []
    users: List[User] = []

    def total_books(self) -> int:
        return len(self.books)

def log_operation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        operation = func.__name__
        try:
            result = func(*args, **kwargs)
            print(f"Операция '{operation}' выполнена успешно.")
            return result
        except Exception as e:
            print(f"Ошибка при выполнении операции '{operation}': {e}")
            raise
    return wrapper

if __name__ == "__main__":
    book1 = Book(
        title="Преступление и наказание",
        author="Фёдор Достоевский",
        year=1866,
        categories=["Роман", "Психологическая драма", "Классика"]
    )

    book2 = Book(
        title="Мастер и Маргарита",
        author="Михаил Булгаков",
        year=1967,
        categories=["Фантастика", "Сатира", "Классика"]
    )

    user1 = User(
        name="Анна Каренина",
        email="anna.karenina@example.com",
        membership_id="M98765"
    )

    library = Library(books=[book1, book2], users=[user1])

    add_book(Book(
        title="Война и мир",
        author="Лев Толстой",
        year=1869,
        categories=["Исторический роман", "Классика"]
    ))

    found = find_book("Война и мир")
    print("Найдена:", found)

    try:
        is_book_borrow("Война и мир")
    except BookNotAvailable as e:
        print("Ошибка:", e)

    return_book("Война и мир")

    print("Всего книг в библиотеке:", library.total_books())