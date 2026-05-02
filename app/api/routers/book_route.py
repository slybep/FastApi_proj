from app.api.dependencies import get_book_service
from app.schemas.book import BookCreateDTO, BookSchema
from app.services.book import BookService, NotFoundError
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(prefix="/books")


@router.get("")
def read_books(
    book_service: BookService = Depends(get_book_service),
) -> list[BookSchema]:
    return book_service.list_book()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_book(
    DTO: BookCreateDTO, book_service: BookService = Depends(get_book_service)
) -> BookSchema:
    return book_service.create_book(DTO)


@router.put("/{id}")
def change_book(
    id: str, DTO: BookCreateDTO, book_service: BookService = Depends(get_book_service)
) -> BookSchema:
    try:
        result = book_service.update_book(id=id, book_update=DTO)
    except NotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return result


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: str, book_service: BookService = Depends(get_book_service)) -> None:
    try:
        book_service.delete_book(id=id)
    except NotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
