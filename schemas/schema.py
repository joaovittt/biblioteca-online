from typing import Optional
import datetime as dt 
import pydantic

class UserSchema(pydantic.BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    full_name: str
    user_name: str
    email: str
    phone_ddd: str
    phone_number: str
    cpf: str
    date_created: dt.datetime
    hashed_pass: str

    class Config:
        orm_mode = True