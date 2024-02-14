from fastapi import APIRouter

from backend.api.models import DateModel
from backend.logic.preferred_date_generator import calculate_best_date

router = APIRouter(prefix="/dates")


@router.get("")
def get_date(attraction: str, dates: DateModel, city: str):
    return calculate_best_date(attraction, dates, city)
