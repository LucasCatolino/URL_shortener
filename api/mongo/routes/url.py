from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from mongo.mongo_connection import (
    add_url,
    #retrieve_url,
    retrieve_url_short
)
from mongo.models.url import (
    ErrorResponseModel,
    ResponseModel,
    URLSchema,
)

router = APIRouter()


#Create
@router.post("/", response_description="URL data added into the database")
async def add_url_data(url: URLSchema = Body(...)):
    url = jsonable_encoder(url)
    new_url = await add_url(url)
    return ResponseModel(new_url, "URL added successfully.")


#Read
@router.get("/{url_short}", response_description="URL data retrieved")
async def get_url_data_short(url_short):
    url = await retrieve_url_short(url_short)
    if url:
        return ResponseModel(url, "URL data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "URL doesn't exist.")