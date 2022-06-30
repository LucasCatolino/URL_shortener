import sys
from datetime import timedelta
import json
from fastapi.encoders import jsonable_encoder

import redis

from mongo.mongo_connection import retrieve_url_short

#Connection
def redis_connect() -> redis.client.Redis:
    try:
        client = redis.Redis(
            host="localhost",
            port=6379,
            db=0,
        )
        ping = client.ping()
        if ping is True:
            print("Connection OK!")
            return client
    except redis.ConnectionError:
        print("Connection Error!")
        sys.exit(1)


client = redis_connect()

#Helpers
def get_routes_from_cache(key: str) -> str:
    #Data from redis
    val = client.get(key)
    return val


def set_routes_to_cache(key: str, value: str) -> bool:
    #Data to redis
    state = client.setex(
        key,
        timedelta(hours=24),
        value=value,
    )
    return state


async def get_from_redis_cache(url: str) -> dict:
    # First it looks for the data in redis cache
    data = get_routes_from_cache(url)

    # If cache is found then serves the data from cache
    if data is not None:
        return data
    
    else:
        # If cache is not found then sends request to Mongo Api
        data = await retrieve_url_short(url) #'mongo' #await get_from_mongo(url) #TODO: si no esta en Redis, buscar en Mongo

        # Saves the respose to redis and serves it directly
        returning_url= jsonable_encoder(data)['url_long']
        state = set_routes_to_cache(key= url, value= returning_url)

        if state is True:
            return returning_url
        return data


async def set_to_redis(url_short: str, url: str) -> dict:
    state= set_routes_to_cache(url_short, url)
    if state is True:
        return json.dumps(state)
    return state

async def get_from_redis(url: str) -> dict:
    state= get_routes_from_cache(url)
    if state is True:
        return json.dumps(state)
    return state

    """
    #TODO: eliminar esto
    async def set_to_redis_inf(url_short: str, url: str) -> dict:
    state= client.set(
        url_short,
        value=url,
    )
    if state is True:
        return json.dumps(state)
    return state
    """