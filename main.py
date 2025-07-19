from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def default_route():
    return {"message": "API for this core is running"}
