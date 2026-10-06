from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class AIn(BaseModel):
    patient_id: int
    ward_id: int
    admitted: date
    diagnosis: str | None = None

@router.post("/")
def admit(data: AIn, db: Session = Depends(get_session)):
    ward = db.execute(text("SELECT beds FROM wards WHERE id=:i"), {"i": data.ward_id}).fetchone()
    if not ward: raise HTTPException(404, "Палата не найдена")
    occupied = db.execute(text("SELECT COUNT(*) FROM admissions WHERE ward_id=:i AND status='active'"),
                          {"i": data.ward_id}).fetchone()[0]
    if occupied >= ward[0]: raise HTTPException(400, "Палата переполнена")
    row = db.execute(text("""
        INSERT INTO admissions (patient_id, ward_id, admitted, diagnosis)
        VALUES (:patient_id,:ward_id,:admitted,:diagnosis) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.post("/{adm_id}/discharge")
def discharge(adm_id: int, cost: float, db: Session = Depends(get_session)):
    db.execute(text("""
        UPDATE admissions SET discharged=CURRENT_DATE, cost=:c, status='closed' WHERE id=:i
    """), {"c": cost, "i": adm_id})
    db.commit()
    return {"status": "discharged"}
