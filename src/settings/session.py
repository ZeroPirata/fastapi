from sqlalchemy.orm import sessionmaker
from typing import Generator
from sqlalchemy import create_engine

from settings.settings import settings  # Importe engine diretamente

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()