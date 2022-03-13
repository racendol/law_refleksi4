from pydantic import BaseModel

class UserBase(BaseModel):
    nama: str
    alamat: str

class UserCreate(UserBase):
    npm: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
