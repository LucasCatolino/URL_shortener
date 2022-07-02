from fastapi import FastAPI
from red.routes.urls import router as UrlRouter
from mongo.routes.url import router as UrlRouterMongo
from mongo.routes.access_log import router as AccessLogRouter
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

#Cors origins
origins = [
    "http://localhost",
    "http://localhost:8080",
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Redis endpoints
app.include_router(UrlRouter, tags=["URL"], prefix="/url")

#Mongo endpoints
app.include_router(UrlRouterMongo, tags=["URL"], prefix="/url_mongo")
app.include_router(AccessLogRouter, tags=["Access log"], prefix="/access_log")

@app.get("/")
def read_root():
    return {"URL shortening version": "1.0"}