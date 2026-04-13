from datetime import UTC, datetime
from sqlalchemy import delete, select, update
from sqlalchemy import Session, aliased 
from . import models, schemas

def get_stations(db: Session, code: str | None = None):
    stm = select(models.Station)
    if code is not None:
        stm = stm.where(models.Station.code.ilike(code))
    return db.scalars(stm).all()
