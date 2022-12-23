
from redis_om import get_redis_connection, JsonModel #HashModel
from typing import Union, List
# from pydantic import BaseModel

redis = get_redis_connection(
    host="redis-11271.c305.ap-south-1-1.ec2.cloud.redislabs.com",
    port=11271,
    password="NtC3b2QkRA5cUQdzKkxpXiVuMm6wC4Lp",
    decode_responses=True)


class Video(JsonModel):
    user_video_id: str
    user_video_transcript: Union[List, None] = None


    class Meta:
        database = redis

