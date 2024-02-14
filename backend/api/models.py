from pydantic import BaseModel


class DateModel(BaseModel):
    start_date: str
    end_date: str
