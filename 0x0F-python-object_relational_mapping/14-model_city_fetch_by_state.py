#!/usr/bin/python3
"""
script that prints all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]
    ))
    session = sessionmaker(bind=engine)
    Session = session()
    cities = Session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
