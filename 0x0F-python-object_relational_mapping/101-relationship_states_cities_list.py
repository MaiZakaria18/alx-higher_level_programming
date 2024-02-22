#!/usr/bin/python3
""""
script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State, Base
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]
    ))
    session = sessionmaker(bind=engine)
    Session = session()
    Base.metadata.create_all(engine)
    states = Session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
