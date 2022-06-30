from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from mongo.mongo_connection import (
    add_access_log
)
from mongo.models.access_log import (
    ErrorResponseModel,
    ResponseModel,
    AccessLogSchema,
)

router = APIRouter()

#Create
@router.post("/", response_description="Access log data added into the database")
async def add_access_lg_data(access_log: AccessLogSchema = Body(...)):
    access_log = jsonable_encoder(access_log)
    new_access_log = await add_access_log(access_log)
    return ResponseModel(new_access_log, "Access log added successfully.")