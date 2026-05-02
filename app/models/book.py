from sqlalchemy.orm import Mapped

from .base import Base


class BookORM(Base):
    __tablename__ = "books"
    name: Mapped[str]
