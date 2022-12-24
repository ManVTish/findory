
from redis_om import get_redis_connection, JsonModel #HashModel
from typing import Union, List
# from pydantic import BaseModel

redis = get_redis_connection(
    host="",
    port="",
    password="",
    decode_responses=True)


class Video(JsonModel):
    user_video_id: str
    user_video_transcript: Union[List, None] = None


    class Meta:
        database = redis

