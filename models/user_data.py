from pydantic import BaseModel

class UserData(BaseModel):
    main_video_id: str
    keyword: str

