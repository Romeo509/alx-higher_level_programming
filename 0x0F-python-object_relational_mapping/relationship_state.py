#!/usr/bin/python3
"""
Module that defines the State class.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """State class with a relationship to City."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', backref='state', cascade='all, delete-orphan'
    )

    def __repr__(self):
        """Return a string representation of the State object."""
        return "{}: {}".format(self.id, self.name)
