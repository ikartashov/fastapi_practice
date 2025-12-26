# Работа с БД через sqlalchemy и в docker
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.db_models import Base

from dotenv import load_dotenv
load_dotenv()
DB_URL = os.getenv("DB_URL")
if not DB_URL: raise RuntimeError("DB_URL не задан")

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)


def get_session():
    return SessionLocal()
