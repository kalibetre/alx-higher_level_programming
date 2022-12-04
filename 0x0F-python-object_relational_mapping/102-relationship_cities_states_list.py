#!/usr/bin/python3
"""102-relationship_states_cities module
contains a script to list all city objects and their state
"""
from sys import argv

from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_all_cities(session):
    """lists all cities

    Args:
        session (session): sqlalchemy session
    """
    cities = session.query(City).order_by(City.id)
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    list_all_cities(session)
    session.close()
