#!/usr/bin/python3
"""
city Class for table cities
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """
    A class representing a city in a database.

    This class defines the structure of the 'cities' table in the database.
    Each instance of this class corresponds to a row in the 'cities' table.

    Attributes:
        id (int): The unique identifier for the city. This is the primary key.
        name (str): The name of the city.
        state_id (int): The foreign key referencing the id of
        the associated state.

    Args:
        Base: The declarative base class provided by SQLAlchemy.

    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
    state = relationship(State)
