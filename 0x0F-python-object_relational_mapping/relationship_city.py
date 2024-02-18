#!/usr/bin/python3
"""Contains the City class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Class representing the cities table"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
