from fastapi import FastAPI
from red.routes.urls import router as UrlRouter
from mongo.routes.student import router as StudentRouter
from mongo.routes.url import router as UrlRouterMongo


app = FastAPI()

#Redis endpoints
app.include_router(UrlRouter, tags=["URL"], prefix="/url")

#Mongo endpoints
#app.include_router(StudentRouter, tags=["Student"], prefix="/student")
app.include_router(UrlRouterMongo, tags=["URL"], prefix="/url_mongo")

@app.get("/")
def read_root():
    return {"Welcome to": "URL short"}
