#!/usr/bin/python3
"""101-relationship_states_cities module
contains a script to list all state objects and their cities
"""
from sys import argv

from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_all_states_with_cities(session):
    """lists all states together with their cities

    Args:
        session (session): sqlalchemy session
    """
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    list_all_states_with_cities(session)
    session.close()
