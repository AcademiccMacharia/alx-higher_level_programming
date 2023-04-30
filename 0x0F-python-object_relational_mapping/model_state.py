#!/usr/bin/python3

"""
Defines the model of State
"""
from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.orm import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """
    Class with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
