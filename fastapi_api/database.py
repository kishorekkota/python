from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

print("Database URL:", DATABASE_URL)


database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=true, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata = metadata