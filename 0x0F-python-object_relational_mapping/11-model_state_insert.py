#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]
    ))
    session = sessionmaker(bind=engine)
    Session = session()
    new_instance = State(name='Louisiana')
    Session.add(new_instance)
    Session.commit()
    print(new_instance.id)
