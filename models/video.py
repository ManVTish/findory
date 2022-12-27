# from config.database import redis

from redis_om import JsonModel
from models.common_lib import Optional, BaseModel, List

class Video(BaseModel):
    user_video_id: str
    user_video_transcript: Union[List, None] = None


    class Meta:
        database = redis

