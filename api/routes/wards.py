from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class WIn(BaseModel):
    dept_id: int
    number: str
    beds: int
    floor: int | None = None

@router.post("/")
def create(data: WIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO wards (dept_id, number, beds, floor)
        VALUES (:dept_id,:number,:beds,:floor) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/dept/{dept_id}")
def by_dept(dept_id: int, db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(
        text("SELECT * FROM wards WHERE dept_id=:d"), {"d": dept_id}).fetchall()]
