from fastapi import FastAPI
from Forum.database import Base, engine
from Forum.routers import posts

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(posts.router)
