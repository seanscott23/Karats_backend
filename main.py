from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from routers import userinfo
from Reuse import audio
import config
import pyrebase
import pymongo
from fastapi.middleware.cors import CORSMiddleware
import os
from Reuse import gems
import uvicorn

# settings = config.Settings()
app = FastAPI()

# origins = [
#   "http://localhost:3000/*",
#   "http://localhost:3000",
#   "http://www.karatsapp.com",
# ]

# app.add_middleware(
#   CORSMiddleware,
#   allow_origins=origins,
#   allow_credentials=True,
#   allow_methods=["*"],
#   allow_headers=["*"],
# )

# app.include_router(userinfo.router)
# app.include_router(audio.router)
# app.include_router(gems.router)


@app.get("/")
def welcome():
    return "Hello world"


# firebaseConfig = {
#   "apiKey": settings.API_KEY,
#   "authDomain": settings.AUTH_DOMAIN,
#   "databaseURL": settings.DATABASE_URL,
#   "projectId": settings.PROJECT_ID,
#   "storageBucket": settings.STORAGE_BUCKET,
#   "messagingSenderId": settings.MESSAGING_SENDER_ID,
#   "appId": settings.APP_ID,
#   "measurementId": settings.MEASUREMENT_ID
# };

firebaseConfig = {
  "apiKey": os.environ.get("API_KEY_TEST"),
  "authDomain": os.environ.get("AUTH_DOMAIN_TEST"),
  "databaseURL": os.environ.get("DATABASE_URL_TEST"),
  "projectId": os.environ.get("PROJECT_ID_TEST"),
  "storageBucket": os.environ.get("STORAGE_BUCKET_TEST"),
  "messagingSenderId": os.environ.get("MESSAGING_SENDER_ID_TEST"),
  "appId": os.environ.get("APP_ID_TEST"),
  "measurementId": os.environ.get("MEASUREMENT_ID_TEST")
};



firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()
database = firebase.database()


@app.post("/api/get/all/")
def get_gems_by_user():
    try:
      array_of_user_gems = []
      all_gems = database.child("GEMS").get("#$#4")
      if type(all_gems) != 'NoneType':
        for x in all_gems.pyres:
              print(x)
            # if x.item[1]["ownerID"] == gem.ownerID:
            array_of_user_gems.append(x.item)
        return array_of_user_gems
    except:
      return "Database is empty"

# if __name__ == '__main__':
#    app.run()


