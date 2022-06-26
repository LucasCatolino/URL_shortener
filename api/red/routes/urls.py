from fastapi import APIRouter

from red.redis_connection import get_from_redis, set_to_redis_expiring, set_to_redis_inf
#from red.redis_connection import set_to_redis

router = APIRouter()

#Read
@router.get("/{url}")
async def get_url(url: str):
    return await get_from_redis(url)

#Create with expiration time
@router.post("/{url_short}={url}&time={time}")
async def post_url(url_short: str, url: str, time: float):
    return await set_to_redis_expiring(url_short, url, time)

#Create without expiration time
@router.post("/{url_short}={url}?1")
async def post_url(url_short: str, url: str):
    return await set_to_redis_inf(url_short, url)