#!/usr/bin/python3
"""
script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]
    ))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    Session = session()
    new_state = State(name='California')
    Session.add(new_state)
    new_city = City(name='San Francisco', state=new_state)
    Session.add(new_city)
    Session.commit()
