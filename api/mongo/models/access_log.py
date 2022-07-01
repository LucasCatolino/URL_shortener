from pydantic import BaseModel, Field


class AccessLogSchema(BaseModel):
    url_id: str = Field(...)
    device: str = Field(None)
    ip: str = Field(None)
    location: str = Field(None)
    creation_time: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "url_id": "62bdf20e63a1cfb8521231d0",
                "device": "Moto G1",
                "ip": "127.0.0.1",
                "location": "Argentina",
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