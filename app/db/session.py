from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


#Crea el motor de la base de datos.
engine = create_engine(settings.database_url)


#Crea una clase de sesion de base de datos.
SessionLocal = sessionmaker(bind=engine)

#La funcion get_db() crea una sesion de base de datos y la cierra al finalizar.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()