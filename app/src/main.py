from typing import List, Tuple

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud
from .database import SessionLocal


app = FastAPI()


def get_db():  # Dependency
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/hotspot-habitats/", response_model=List[Tuple[str, int]])
def read_hotspot_habitats(db: Session = Depends(get_db)):
    return crud.get_hotspot_habitats(db)


@app.get("/hotspot-habitats/{country}", response_model=List[Tuple[str, int]])
def read_hotspot_habitats_by_country(
    country: str, db: Session = Depends(get_db)
):
    return crud.get_hotspot_habitat_by_country(db, country=country)


@app.get("/")
async def root():
    return {"message": "Hello World"}
