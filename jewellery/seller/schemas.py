from datetime import datetime

from pydantic import BaseModel


class user(BaseModel):
    user_id: int
    email: str
    password: str
    name: str
    surname: str
    role: str
    user_mobile_number: str
    user_gst_number: str
    user_shop_name: str
    user_address: str
    user_city: str
    user_state: str
    role: str
    register_date: datetime


class user_request(BaseModel):
    user_request_id: int
    status: str | None = 'pending'
    description: str | None = ''

