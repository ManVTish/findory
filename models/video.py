# from config.database import redis

from models.common_lib import Optional, BaseModel, List
from models.time_stamps import TimeStamps

class Video(BaseModel):
    source_video_id: str
    user_id: str
    keyword: str
    transcripts: Optional[List] = None
    time_stamp: TimeStamps[List]

