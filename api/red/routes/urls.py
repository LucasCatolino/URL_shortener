from fastapi import APIRouter

from red.redis_connection import get_from_redis
from red.redis_connection import set_to_redis

router = APIRouter()

#Read
@router.get("/redis/{url}")
async def get_url(url: str):
    return await get_from_redis(url)

#Create
@router.post("/redis/{url_short}={url}")
async def post_url(url_short: str, url: str):
    return await set_to_redis(url_short, url)