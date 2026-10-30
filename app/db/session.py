from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


#Creates the database engine.
engine = create_engine(settings.database_url)


#Creates a sessionmaker that will be used to create database sessions.
SessionLocal = sessionmaker(bind=engine)

#The get_db() function creates a database session and closes it when finished.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()