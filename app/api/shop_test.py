from fastapi import APIRouter

router = APIRouter()

@router.get("/shop")
async def get_shop():
    return {"message": "Shop API"}