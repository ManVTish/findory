from config.database import redis

from redis_om import JsonModel
from typing import Union, List
# from pydantic import BaseModel


class Video(JsonModel):
    user_video_id: str
    user_video_transcript: Union[List, None] = None


    class Meta:
        database = redis

