from fastapi import FastAPI
from app.api import api_router

# 创建主路由器
app = FastAPI()

# 注册路由
app.include_router(api_router)