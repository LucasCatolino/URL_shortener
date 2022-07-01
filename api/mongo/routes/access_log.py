from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from mongo.mongo_connection import (
    add_access_log,
    retrieve_access_logs,
    retrieve_locations,
    retrieve_id
)
from mongo.models.access_log import (
    ErrorResponseModel,
    ResponseModel,
    AccessLogSchema,
)

router = APIRouter()

#Create
@router.post("/", response_description="Access log data added into the database")
async def add_access_log_data(access_log: AccessLogSchema = Body(...)):
    access_log = jsonable_encoder(access_log)
    new_access_log = await add_access_log(access_log)
    return ResponseModel(new_access_log, "Access log added successfully.")

#Read
@router.get("/", response_description="Access log data retrieved")
async def get_access_logs():
    access_logs = await retrieve_access_logs()
    if access_logs:
        return ResponseModel(access_logs, "Access log data retrieved successfully")
    return ResponseModel(access_logs, "Empty list returned")

#Read
@router.get("/locations/{url_id}", response_description="Locations data retrieved")
async def get_locations(url_id):
    locations = await retrieve_locations(url_id)
    if locations:
        return ResponseModel(locations, "Locations data retrieved successfully")
    return ResponseModel(locations, "Empty list returned")

#Read
@router.get("/id/{url_short}", response_description="ID retrieved")
async def get_id(url_short):
    id = await retrieve_id(url_short)
    if id:
        return ResponseModel(id, "ID retrieved successfully")
    return ResponseModel(id, "Empty list returned")