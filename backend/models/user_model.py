from core.configs import settings
from sqlalchemy import Column, Integer, String, Boolean, DateTime
import datetime as dt

class UserModel(settings.DBBaseModel):
    __tablename__ = 'users'

    id:int = Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name:str = Column(String(50), index=True)
    last_name:str = Column(String(50), index=True)
    full_name:str = Column(String(100), index=True)
    user_name:str = Column(String(20), unique=True, index=True)
    email:str = Column(String(100), unique=True, index=True)
    phone_ddd:str = Column(String(2), default="", index=True)
    phone_number:str = Column(String(9), default="", index=True)
    cpf:str = Column(String(11), default="", index=True)
    #is_active = Column(Boolean, default=True)
    date_created:dt.datetime = Column(DateTime, default=dt.datetime.utcnow)
    #date_last_updated = Column(DateTime, default=dt.datetime.utcnow)
    hashed_pass:str = Column(String)

    def verify_pass(self, password:str):
        return hash.bcrypt.verify(password, self.hashed_pass)