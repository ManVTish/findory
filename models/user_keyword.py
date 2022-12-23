# from pydantic import BaseModel
from models.video import redis, JsonModel

class UserKeyword(JsonModel):
    keyword: str
    key_id: str

    class Meta:
        database = redis

