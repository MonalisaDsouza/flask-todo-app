import os
from dotenv import load_dotenv


if os.getenv("FLASK_ENV") != "production":
    load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
