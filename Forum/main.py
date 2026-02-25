from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/posts")
def create_post(post: schemas.TravelPostCreate, db: Session = Depends(get_db)):
    db_post = models.TravelPost(
        country=post.country,
        total_cost=post.total_cost,
        food=post.breakdown.food,
        accommodation=post.breakdown.accommodation,
        transport=post.breakdown.transport,
        attractions=post.breakdown.attractions,
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@app.get("/posts")
def list_posts(db: Session = Depends(get_db)):
    return db.query(models.TravelPost).all()
