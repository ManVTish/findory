
from redis_om import get_redis_connection, JsonModel #HashModel
from typing import Union, List
# from pydantic import BaseModel

redis = get_redis_connection(
    host = REDIS_STORAGE_HOST,
    port = REDIS_PORT,
    password = REDIS_STORAGE_PASSWORD,
    decode_responses = True)


class Video(JsonModel):
    user_video_id: str
    user_video_transcript: Union[List, None] = None


    class Meta:
        database = redis

