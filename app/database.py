from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# If you want to use psycopg2 instead of sqlalchemy
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi',
#                                 user='postgres', password='Password', cursor_factory=RealDictCursor)

#         cursor = conn.cursor()

#         print('Database connection was successful')

#         break

#     except Exception as error:

#         print('Connecting to database failed')

#         print('Error:', error)

#         time.sleep(2)
