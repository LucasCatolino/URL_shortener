import sys
from datetime import timedelta
import json

import redis

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
    """Data from redis."""

    val = client.get(key)
    return val


def set_routes_to_cache(key: str, value: str, time: float) -> bool:
    """Data to redis."""

    state = client.setex(
        key,
        timedelta(hours=time),
        value=value,
    )
    return state


async def get_from_redis_cache(url: str) -> dict:

    url = {"url": url}

    # First it looks for the data in redis cache
    data = get_routes_from_cache(key=json.dumps(url))
    print(data)
    print(type(data))

    # If cache is found then serves the data from cache
    if data is not None:
        data = data.decode("UTF-8")
        data_dict = json.loads(data)
        print(data_dict)
        print(type(data_dict))
        data_dict["cache"] = True
        return data_dict

async def set_to_redis_expiring(url_short: str, url: str, time: float) -> dict:
    state= set_routes_to_cache(url_short, url, time)
    if state is True:
        return json.dumps(state)
    return state

async def get_from_redis(url: str) -> dict:
    state= get_routes_from_cache(url)
    if state is True:
        return json.dumps(state)
    return state

async def set_to_redis_inf(url_short: str, url: str) -> dict:
    state= client.set(
        url_short,
        value=url,
    )
    if state is True:
        return json.dumps(state)
    return state