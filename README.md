# Awesome URL shortener
The idea of this project is to create a polyglot solution to the problem of long and user-unfriendly URLs. For this solution Redis and MongoDB where used to store URLs and stadistics about clicks.
Redis was used as a key-value database (key: short URL, value: long URL), and MongoDB was used to store clicks' information such as date of click, device, etc.

## Contents
- [Prerequisites](#prerequisites)
- [Running the project](#running-the-project)
- [Swagger](#swagger)

## Prerequisites
In order to run this project, user must have installed:
- [Python](https://www.python.org/downloads/)
- [FastAPI](https://fastapi.tiangolo.com/#installation)
    ```
    pip install fastapi
    pip install "uvicorn[standard]"
    ```
- [Docker](https://docs.docker.com/engine/install/) (not mandatory but highly recommended)
- [MongoDB](https://hub.docker.com/_/mongo)
    ```
    docker pull mongo
    docker run --name Mymongo –p 27017:27017 -d mongo
    ```
- [Redis](https://hub.docker.com/_/redis)
    ```
    docker pull redis
    docker run --name Myredis -p 6379:6379 -d redis
    ```

## Running the project
1. Start Docker
2. Start MongoDB
    ```
    docker start Mymongo
    ```
3. Start Redis
    ```
    docker start Myredis
    ```
4. Start API
    From the main path:
    ```
    uvicorn main:app --reload
    ```

## Swagger
In case of wanting to read API documentation or test endpoints manually, Swagger may be found in [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)