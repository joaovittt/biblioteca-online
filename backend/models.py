import datetime as dt

import sqlalchemy as sql
import sqlalchemy.orm as orm 
import passlib.hash as hash

import database as db

class user(db.Base):
    __tablename__ = "users"
    id = sql.column(sql.Integer, primary_key = True, index=True)
    email = sql.column(sql.String, unique=True, index=True)
    hashed_pass = sql.Column(sql.String)

    def verify_pass(self, password:str):
        return hash.bcrypt.verify(password, self.hashed_pass)
    

