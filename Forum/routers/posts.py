from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from Forum import models, schemas
from Forum.database import get_db

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("")
def create_post(post: schemas.TravelPostCreate, db: Session = Depends(get_db)):
    """Create a new post (C)"""
    db_post = models.TravelPost(
        country=post.country,
        total_cost=post.total_cost,
        food=post.food,
        accommodation=post.accommodation,
        transport=post.transport,
        attractions=post.attractions,
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.get("", response_model=list[schemas.TravelPostResponse])
def list_posts(db: Session = Depends(get_db)):
    """read all posts (R)"""
    return db.query(models.TravelPost).all()


@router.get("/{post_id}", response_model=schemas.TravelPostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    """ Read a post (R)"""
    post = db.query(models.TravelPost).filter(models.TravelPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/{post_id}", response_model=schemas.TravelPostResponse)
def update_post(post_id: int, updated: schemas.TravelPostCreate, db: Session = Depends(get_db)):
    """Update a post (U)"""
    post = db.query(models.TravelPost).filter(models.TravelPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    post.country = updated.country
    post.total_cost = updated.total_cost
    post.food = updated.food
    post.accommodation = updated.accommodation
    post.transport = updated.transport
    post.attractions = updated.attractions
    post.souvenirs = updated.souvenirs

    db.commit()
    db.refresh(post)
    return post


@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    """Delete a post (D)"""
    post = db.query(models.TravelPost).filter(models.TravelPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    db.delete(post)
    db.commit()
    return {"message": "Post deleted"}


