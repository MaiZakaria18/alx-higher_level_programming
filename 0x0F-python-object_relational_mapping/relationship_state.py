##!/usr/bin/python3
"""
file that contains the class definition of a State and an
instance Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()


class State(Base):
    """class represnting states table"""

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    """cities contain objects of City class"""
    cities = relationship('City', back_populates='state',
                          cascade="delete, all")
    from relationship_city import City
