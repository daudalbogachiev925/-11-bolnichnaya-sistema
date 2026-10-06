from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class PrIn(BaseModel):
    admission_id: int
    drug: str
    dosage: str | None = None
    duration_days: int | None = None

@router.post("/")
def create(data: PrIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO prescriptions (admission_id, drug, dosage, duration_days)
        VALUES (:admission_id,:drug,:dosage,:duration_days) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/admission/{adm_id}")
def by_admission(adm_id: int, db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(
        text("SELECT * FROM prescriptions WHERE admission_id=:i"), {"i": adm_id}).fetchall()]
