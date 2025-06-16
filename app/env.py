# app/env.py
from pydantic_settings import BaseSettings

class Env(BaseSettings):
    PG_DATABASE_URL:str = "postgresql+psycopg2://rancy@localhost:5432/shop_db"


env = Env()