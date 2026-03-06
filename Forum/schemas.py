from pydantic import BaseModel
from typing import Optional

class TravelPostBase(BaseModel):
    country: str
    total_cost: Optional[float] = None
    food: Optional[float] = None
    accommodation: Optional[float] = None
    transport: Optional[float] = None
    attractions: Optional[float] = None
    souvenirs: Optional[float] = None


class TravelPostCreate(TravelPostBase):
    pass

class TravelPostResponse(TravelPostBase):
    id: int

    class Config:
        from_attributes = True
