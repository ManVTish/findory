
from models.notes import Notes, Optional, BaseModel

class TimeStamps(BaseModel):
    video_pk_id: str
    user_id: str
    notes: Notes
    start_time: str
    end_time: str

