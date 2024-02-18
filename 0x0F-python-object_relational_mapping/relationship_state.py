#!/usr/bin/python3
"""Contains the State class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """Class representing the states table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(256), nullable=False)
    cities = relationship(
          "City", backref="state", cascade="all, delete-orphan"
    )
