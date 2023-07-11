from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base

db_endpoint = 'database-1.clllywvqw34m.us-east-2.rds.amazonaws.com'
db_port = 5432
db_name = 'postgres'
db_user = 'postgres'
db_password = 'biblio123'

class Settings(BaseModel):
    API_V1_STR: str = '/api/v1'
    DB_URL: str  = f'postgresql+asyncpg://{db_user}:{db_password}@{db_endpoint}:{db_port}/{db_name}'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
