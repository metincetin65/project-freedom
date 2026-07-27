import app.models

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.base import Base

DATABASE_URL = "sqlite:///project_freedom.db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)


def create_tables():
    Base.metadata.create_all(bind=engine)