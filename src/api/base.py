from fastapi import APIRouter

from api.v1 import user_route


api_router = APIRouter()
api_router.include_router(user_route.router,prefix="",tags=["users"])