from app.models.book import BookORM
from sqlalchemy import select
from sqlalchemy.orm import Session


class BookRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[BookORM]:
        return self.db.scalars(select(BookORM)).all()

    def get_by_id(self, book_id: str) -> BookORM:
        return self.db.get(BookORM, book_id)

    def create(self, name: str) -> BookORM:
        book = BookORM(name=name)
        self.db.add(book)
        self.db.flush()
        return book

    def delete(self, BookORM) -> None:
        self.db.delete(BookORM)
