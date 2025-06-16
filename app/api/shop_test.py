from fastapi import APIRouter,Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.core.pq_db import get_db

router = APIRouter()

@router.get("/shop")
async def get_shop(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM products"))
    rows = result.fetchall()  # 拿到所有结果
    items = [dict(row._mapping) for row in rows]  # 转换成列表的字典
    return {"items": items}