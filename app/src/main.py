from typing import Dict, List

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud
from .database import SessionLocal


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():  # Dependency
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/hotspot-habitats/", response_model=List[Dict])
def read_hotspot_habitats(db: Session = Depends(get_db)):
    return crud.get_hotspot_habitats(db)


@app.get("/hotspot-habitats/{country}", response_model=List[Dict])
def read_hotspot_habitats_by_country(
    country: str, db: Session = Depends(get_db)
):
    return crud.get_hotspot_habitat_by_country(db, country=country)


@app.get("/threats/", response_model=List[Dict])
def read_threats(db: Session = Depends(get_db)):
    return crud.get_threats(db)


@app.get("/threats/{habitat_code}", response_model=List[Dict])
def read_threats_by_habitat_code(
    habitat_code: str, db: Session = Depends(get_db)
):
    return crud.get_threats_by_habitat(db, habitat_code=habitat_code)


@app.get("/")
async def root():
    return {"message": "Hello World"}
