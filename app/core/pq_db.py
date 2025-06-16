# app/core/pg_db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.env import env

# 创建引擎
engine = create_engine(env.PG_DATABASE_URL, pool_pre_ping=True)

# 创建Session类，后面每个请求独享一个Session实例
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 依赖函数，FastAPI注入用
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()