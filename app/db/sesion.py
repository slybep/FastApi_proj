import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()
settings = os.getenv("DATABASE_URL")
engine = create_engine(settings)
Sessionlocal = sessionmaker(bind=engine)


def Get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
