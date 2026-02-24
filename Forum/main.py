from fastapi import FastAPI
from schemas import TravelPostResponse

app = FastAPI()

posts = []

@app.get("/")
def root():
    return {"message": "Travel Forum Works!!"}

@app.post("/posts")
def create_post(post: TravelPostResponse) :
    posts.append(post)
    return {"message": "Dodano wpis!", "posts": posts}

@app.get("/posts")
def list_posts():
    return posts
