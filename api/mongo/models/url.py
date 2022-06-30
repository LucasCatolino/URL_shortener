from typing import Optional
import datetime
from bson import List

from pydantic import BaseModel, Field

"""
class StatsSchema(BaseModel):
    date: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "date": 4,
            }
        }
"""

class URLSchema(BaseModel):
    url_short: str = Field(...)
    url_long: str = Field(...)
    creation_time: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "url_short": "a",
                "url_long": "google.com",
                "creation_time": "2022-06-20"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}


"""
class UpdateUrlModel(BaseModel):
    url_short: Optional[str]
    url_long: Optional[str]
    stats: Optional[List[StatsSchema]]

    class Config:
        schema_extra = {
            "example": {
                "url_short": "aa",
                "url_long": "google.com",
                "stats": ["date"],
                "gpa": "4.0",
            }
        }
"""