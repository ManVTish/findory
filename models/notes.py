from pydantic import BaseModel
from typing import Optional

class Notes(BaseModel):
    user_id: str
    time_stamp_id: str
    description: text

