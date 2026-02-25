from sqlalchemy import Column, Integer, String, Float
from database import Base

class TravelPost(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=True)
    total_cost = Column(Float)

    food = Column(Float)
    accommodation = Column(Float)
    transport = Column(Float)
    attractions = Column(Float)
