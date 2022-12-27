from models.common_lib import Optional, BaseModel
from models.notes import Notes

class TimeStamps(BaseModel):
    video_pk_id: str
    user_id: str
    notes: Notes
    start_time: str
    end_time: str

