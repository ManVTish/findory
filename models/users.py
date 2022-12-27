from models.common_lib import Optional, BaseModel, List

class Users(BaseModel):
    username: str
    password: str
    membership: Optional[bool] = false

