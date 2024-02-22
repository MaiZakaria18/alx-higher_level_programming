#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]
    ))
    session = sessionmaker(bind=engine)
    Session = session()
    states = Session.query(State).filter(State.name.contains('a')).all()
    for state in states:
        Session.delete(state)
    Session.commit()
