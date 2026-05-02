from pydantic import BaseModel, ConfigDict


class BookSchema(BaseModel):
    id: str
    name: str
    model_config = ConfigDict(from_attributes=True)


class BookCreateDTO(BaseModel):
    name: str
