from models.common_lib import Optional, BaseModel, List

class Notes(BaseModel):
    user_id: str
    time_stamp_id: str
    description: str

