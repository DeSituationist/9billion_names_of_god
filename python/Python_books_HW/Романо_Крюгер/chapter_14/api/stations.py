from typing import Optional

from fastapi import (APIRouter, Depends, HTTPException, Response, status)

from sqlalchemy.orm import Session

from . import crud
from .deps import get_db
from .schemas import Station, StationCreate, StationUpdate, Train

router = APIRouter(prefix='/stations')

@router.get('', tags=['Stations'])
def get_stations(db: Session = Depends(get_db), code: Optional[str] = None) -> list[Station]:
    return crud.get_stations(db=db, code=code)
