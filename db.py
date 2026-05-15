from typing import Annotated
from fastapi import Depends, FastAPI
from sqlmodel import  Session, SQLModel, create_engine, select
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("DB_URL")

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)


Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        print("db connected")
        yield db
    except Exception as e:
        print("Error is coming while connecting", e)
    finally:
        db.close()

