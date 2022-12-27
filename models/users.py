from pydantic import BaseModel
from typing import Optional

class Users(BaseModel):
    username: str
    password: str
    membership: bool

