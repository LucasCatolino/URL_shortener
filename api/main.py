from fastapi import FastAPI
from red.routes.urls import router as UrlRouter
from mongo.routes.url import router as UrlRouterMongo
from mongo.routes.access_log import router as AccessLogRouter


app = FastAPI()

#Redis endpoints
app.include_router(UrlRouter, tags=["URL"], prefix="/url")

#Mongo endpoints
app.include_router(UrlRouterMongo, tags=["URL"], prefix="/url_mongo")
app.include_router(AccessLogRouter, tags=["Access log"], prefix="/access_log")

@app.get("/")
def read_root():
    return {"URL shortening version": "1.0"}