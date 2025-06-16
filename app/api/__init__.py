from fastapi import APIRouter

from app.api import shop_test

api_router = APIRouter()

api_router.include_router(shop_test.router, prefix="/shop_test", tags=["Shop Test"])

