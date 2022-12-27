from pydantic import BaseModel
from typing import Optional

class TimeStamps(BaseModel):
    video_pk_id: str
    user_id: str
    notes: str # type Notes
    start_time: str
    end_time: str

