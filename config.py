from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    # web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
    # web: uvicorn main:app --reload --host 0.0.0.0 --port ${PORT}
    # web: gunicorn -w 4 -k uvicorn.workers.UvicornH11Worker main:app
    API_KEY: str = os.getenv('API_KEY')
    AUTH_DOMAIN: str = os.getenv('AUTH_DOMAIN')
    DATABASE_URL: str = os.getenv('DATABASE_URL')
    PROJECT_ID: str = os.getenv('PROJECT_ID')
    STORAGE_BUCKET: str = os.getenv('STORAGE_BUCKET')
    MESSAGING_SENDER_ID: str = os.getenv('MESSAGING_SENDER_ID')
    APP_ID: str = os.getenv('APP_ID')
    MEASUREMENT_ID: str = os.getenv('MEASUREMENT_ID')

    class Config:
        env_file = ".env"