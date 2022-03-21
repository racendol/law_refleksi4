from sqlalchemy.orm import Session

import models, schemas

def get_user_by_npm(db: Session, npm: str):
    return db.query(models.User).filter(models.User.npm == npm).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        nama=user.nama,
        npm=user.npm,
        alamat=user.alamat
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: schemas.User, user_update: schemas.UserBase):
    user.nama = user_update.nama
    user.alamat = user_update.alamat
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user: schemas.User):
    db.delete(user)
    db.commit()