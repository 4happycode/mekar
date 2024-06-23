from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, FormDataDB
from shcemas import FormData, FormDataCreate
from typing import List

app = FastAPI()

# Set up CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
    # Add more origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Dependency untuk mendapatkan session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint untuk membuat data baru
@app.post("/create", response_model=FormData)
def create_item(item: FormDataCreate, db: Session = Depends(get_db)):
    try:
        # Periksa apakah identity_number sudah ada di database
        if db.query(FormDataDB).filter(FormDataDB.identity_number == item.identityNumber).first():
            raise HTTPException(status_code=400, detail="Identity number %s already registered"%(item.identityNumber))
        if db.query(FormDataDB).filter(FormDataDB.email == item.email).first():
            raise HTTPException(status_code=400, detail="email %s already registered"%(item.email))
        
        # Simpan data ke dalam database
        db_item = FormDataDB(name=item.name, identity_number=item.identityNumber, email=item.email, date_of_birth=item.dateOfBirth)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint untuk mendapatkan semua data
@app.get("/data", response_model=List[FormData])
def get_data(db: Session = Depends(get_db)):
    return db.query(FormDataDB).all()
