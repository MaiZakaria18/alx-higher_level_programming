#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]
    ))
    session = sessionmaker(bind=engine)
    Session = session()
    try:
        state = Session.query(State).filter(State.name == argv[4]).one()
        print(state.id)
    except Exception:
        print("Not found")
