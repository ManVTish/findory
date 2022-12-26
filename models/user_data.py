from models.video import redis, JsonModel

class UserData(JsonModel):
    main_video_id: str
    keyword: str

