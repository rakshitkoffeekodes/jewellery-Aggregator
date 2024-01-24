from datetime import datetime

from pydantic import BaseModel


class user(BaseModel):
    user_id: int
    email: str
    password: str
    name: str
    surname: str
    role: str
    register_date: datetime

