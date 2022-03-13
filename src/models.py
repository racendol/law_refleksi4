from sqlalchemy import Column, Integer, String

from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String)
    npm = Column(String)
    alamat = Column(String)