from uuid import uuid4
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class BookDTO(BaseModel):
    id : str
    name: str
class BookCreateDTO(BaseModel):
    name : str

book: list[BookDTO] = []
@app.get("/")
def read_books() -> list[BookDTO]:
    return book

@app.post("/")
def create_book(payload: BookCreateDTO) -> BookDTO:
    new_book = BookDTO(id = str(uuid4()),name = payload.name)
    book.append(new_book)
    return new_book
@app.put("/{id}")
def change_book(id: str, payload: BookCreateDTO) -> BookDTO:
    if id == '':
        raise HTTPException(status_code=404, detail='Id is empty')
    
    for i, val in enumerate(book):
        if val.id == id:
            val.name = payload.name
            return book[i]
        raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/{id}")
def delete_book(id: str) -> BookDTO:
    if id == '':
        raise HTTPException(status_code=404, detail='Id is empty')
    
    for i, val in enumerate(book):
        if val.id == id:
            delete = book.pop(i)
            return delete
    raise HTTPException(status_code=404, detail="Book not found")