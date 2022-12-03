#!/usr/bin/python3
"""14-model_city_fetch_by_state module
contains a script to fetch cities from database
"""
from sys import argv

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_all_cities(session):
    instances = session.query(City, State).join(State).order_by(City.id)

    for city, state in instances:
        print(f"{state.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    print_all_cities(session)
    session.close()
