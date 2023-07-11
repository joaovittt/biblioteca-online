from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import database

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
