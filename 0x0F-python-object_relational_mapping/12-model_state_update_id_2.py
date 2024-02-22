#!/usr/bin/python3
"""
script that changes the name of a State object from the
database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]
    ))
    session = sessionmaker(bind=engine)
    Session = session()
    state = Session.query(State).filter(State.id == 2).one()
    state.name = "New Mexico"
    Session.commit()
