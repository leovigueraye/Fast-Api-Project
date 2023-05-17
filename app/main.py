from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# first: py -m pip install fastapi[all]
# run server: uvicorn main(name of file):app(name of fast api instance)
# uvicorn app.main:app --reload: to automatically reload server, only used in development enviroment
# if main inside folder, folder.main:app
# api docs: /docs, /redoc

# tells sqlalchemy to create tables in model.py
# models.Base.metadata.create_all(bind=engine)

description = """
SocialMediaApp API helps you do awesome stuff. 🚀

## Posts

You will be able to:

* **Get posts**. 
* **Create posts**. 
* **Get one post**. 
* **Update post**. 
* **Delete post**. 

## Users

You will be able to:

* **Create user**.
* **Get user**.

## Authentication

You can **authenticate a user**.

## Vote

You can **vote a users post**.
"""


app = FastAPI(
    title="SocialMediaApp",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Leonard the Amazing",
        "url": "https://leovigueraye.netlify.app/",
        "email": "leguriase98@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

# *: all websites can acces this api
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# [path operation]
# decorator to turn a function to an api call
@app.get("/") # << url path
def root():
    return {"message": "welcome to my api"}
