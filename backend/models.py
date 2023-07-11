import datetime as dt

import sqlalchemy as sql
import sqlalchemy.orm as orm
import passlib.hash as hash

import database as db


class User(db.Base):
    __tablename__ = "users"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    email = sql.Column(sql.String, unique=True, index=True)
    hashed_pass = sql.Column(sql.String)

    leads = orm.relationship("Lead", back_populates="owner")

    def verify_pass(self, password: str):
        return hash.bcrypt.verify(password, self.hashed_pass)


class Lead(db.Base):
    __tablename__ = "leads"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    owner_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    first_name = sql.Column(sql.String, index=True)
    last_name = sql.Column(sql.String, index=True)
    email = sql.Column(sql.String, index=True)
    company = sql.Column(sql.String, index=True, default="")
    note = sql.Column(sql.String, default="")
    date_created = sql.Column(sql.DateTime, default=dt.datetime.utcnow)
    date_last_updated = sql.Column(sql.DateTime, default=dt.datetime.utcnow)

    owner = orm.relationship("User", back_populates="Leads")
