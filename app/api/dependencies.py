from app.db.sesion import Get_db
from app.services.book import BookService
from fastapi import Depends
from sqlalchemy.orm import Session


def get_book_service(db: Session = Depends(Get_db)):
    """Функция для инъекции зависимостей"""
    return BookService(db)
