#!/usr/bin/python3

"""
New
"""

from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.orm import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class City(Base):
    """
    Class with id, name and state_id that links to cities
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, foreign_key('state.id'))
