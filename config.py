import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://flaskdb_9h9z_user:lZsAvJOh4IUABUlO6vF0wbMaUw572Pz2@dpg-cvi3vrlds78s73ej7dtg-a.oregon-postgres.render.com/flaskdb_9h9z")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
