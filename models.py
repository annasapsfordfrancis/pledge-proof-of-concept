from xmlrpc.client import Boolean
from app import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# declarative base class
Base = declarative_base()

class User(db.Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    def __str__(self):
        return self.name