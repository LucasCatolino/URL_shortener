from fastapi import FastAPI
from red.routes.urls import router as UrlRouter
from mongo.routes.student import router as StudentRouter

app = FastAPI()

#Redis endpoints
app.include_router(UrlRouter, tags=["URL"], prefix="/url")

#Mongo endpoints
app.include_router(StudentRouter, tags=["Student"], prefix="/student")

@app.get("/")
def read_root():
    return {"Welcome to": "URL short"}
