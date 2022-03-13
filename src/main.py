import os
import aiofiles
from fastapi import Depends, FastAPI, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"description": "API CRUD untuk mengolah data mahasiswa."}

@app.get("/mahasiswa/{npm}")
async def get_mahasiswa(npm: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_npm(db, npm)
    if not db_user:
        raise HTTPException(status_code=400, detail=f"Tidak ditemukan mahasiswa dengan npm: {npm}")
    
    return {db_user}

@app.post("/mahasiswa/")
async def create_mahasiswa(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_npm(db, user.npm)
    if db_user:
        raise HTTPException(status_code=400, detail=f"Sudah ada mahasiswa dengan npm: {user.npm}")

    db_user = crud.create_user(db, user)
    return {
        "status": "success",
        "user": db_user
    }

@app.put("/mahasiswa/{npm}")
async def update_mahasiswa(npm: str, user: schemas.UserBase, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_npm(db, npm)
    if not db_user:
        raise HTTPException(status_code=400, detail=f"Tidak ditemukan mahasiswa dengan npm: {npm}")
    
    db_user = crud.update_user(db, db_user, user)
    return {
        "status": "success",
        "user": db_user
    }

@app.delete("/mahasiswa/{npm}")
async def delete_mahasiswa(npm: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_npm(db, npm)
    if not db_user:
        raise HTTPException(status_code=400, detail=f"Tidak ditemukan mahasiswa dengan npm: {npm}")
    
    crud.delete_user(db, db_user)
    return {
        "status": "success"
    }

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    cwd = os.getcwd()
    filename = f'{cwd}\\uploaded\\{file.filename}'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    async with aiofiles.open(filename, 'wb') as f:
        contents = await file.read()
        await f.write(contents)
    
    return {
        "status": "success"
    }

