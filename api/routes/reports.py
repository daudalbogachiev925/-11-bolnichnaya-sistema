from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

@router.get("/occupancy")
def occupancy(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/bed_occupancy.sql').read())).fetchall()]

@router.get("/revenue")
def revenue(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/revenue.sql').read())).fetchall()]

@router.get("/discharges")
def discharges(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/discharge.sql').read())).fetchall()]
