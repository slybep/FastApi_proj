from app.repositories.book import BookRepository
from app.schemas.book import BookCreateDTO, BookSchema
from sqlalchemy.orm import Session


class NotFoundError(Exception):
    pass


class BookService:
    def __init__(self, db: Session):
        self.db = db
        self.task_repository = BookRepository(self.db)

    def list_book(self) -> list[BookSchema]:
        result = self.task_repository.get_all()
        return [BookSchema.model_validate(book) for book in result]

    def create_book(self, book_create: BookCreateDTO) -> BookSchema:
        result = self.task_repository.create(name=book_create.name)
        self.db.commit()
        return BookSchema.model_validate(result)

    def update_book(self, id: str, book_update: BookCreateDTO) -> BookSchema:
        result = self.task_repository.get_by_id(book_id=id)

        if result is None:
            raise NotFoundError("Book id not fount")

        if book_update.name is not None:
            result.name = book_update.name

        self.db.commit()
        return BookSchema.model_validate(result)

    def delete_book(self, id: str) -> None:
        result = self.task_repository.get_by_id(book_id=id)

        if not result:
            raise NotFoundError("Book id not fount")

        self.task_repository.delete(result)
        self.db.commit()
