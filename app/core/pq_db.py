from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.env import Env


# 创建数据库引擎
engine = create_engine(Env.PG_DATABASE_URL)

# 创建会话工厂
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# 创建基类
Base = declarative_base()

# 创建会话
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()