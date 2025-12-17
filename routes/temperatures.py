from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from crud import get_temperatures
from schemas import TemperatureResponse

router = APIRouter(prefix="/temperatures")


@router.get("/", response_model=list[TemperatureResponse])
def list_temperatures(
    city_id: int | None = None,
    db: Session = Depends(get_db),
):
    return get_temperatures(db, city_id)
