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

settings = config.Settings()
app = FastAPI()

origins = [
  "http://localhost:3000/*",
  "http://localhost:3000",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(userinfo.router)
app.include_router(audio.router)

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
  "apiKey": API_KEY_TEST,
  "authDomain": AUTH_DOMAIN_TEST,
  "databaseURL": DATABASE_URL_TEST,
  "projectId": PROJECT_ID_TEST,
  "storageBucket": STORAGE_BUCKET_TEST,
  "messagingSenderId": MESSAGING_SENDER_ID_TEST,
  "appId": APP_ID_TEST,
  "measurementId": MEASUREMENT_ID_TEST
};



firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()
database = firebase.database()


