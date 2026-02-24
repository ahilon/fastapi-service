from pydantic import BaseModel

class CostBreakdown(BaseModel):
    food: float
    accommodation: float
    transport: float
    attractions: float
    souvenirs: float

class TravelPostResponse(BaseModel):
    country:str
    total_cost:float
    breakdown:CostBreakdown
