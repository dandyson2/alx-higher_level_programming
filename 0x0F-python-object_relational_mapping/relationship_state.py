#!/usr/bin/python3
"""
This script defines a State class and a Base class to work with MySQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base
Base = declarative_base()


class State(Base):
    """
    State class for representing states in a database.

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
        cities (:obj:`City`): The Cities that belong to this State

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
