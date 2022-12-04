#!/usr/bin/python3
"""14-model_city_fetch_by_state module
contains a script to fetch cities from database
"""
from sys import argv

from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_all_cities(session):
    california = State(name="California")
    california.cities = [City(name="San Francisco")]
    session.add(california)
    session.commit()


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    print_all_cities(session)
    session.close()
