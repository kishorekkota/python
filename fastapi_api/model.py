from sqlalchemy import Column, Integer, String
from .database  import Base

class User(Base):
      __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    ssn = Column(String, unique=True, index=True)
    date_of_birth = Column(String, index=True)



