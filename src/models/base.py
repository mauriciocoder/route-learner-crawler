from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base

from src.db import engine

# Base class
class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    
    def save(self):
        Session = sessionmaker(engine)
        with Session.begin() as session:
            self.created_at = datetime.utcnow() # Saving it as UTC
            session.add(self)
        # commits transaction, closes session

Base = declarative_base(cls=Base)
