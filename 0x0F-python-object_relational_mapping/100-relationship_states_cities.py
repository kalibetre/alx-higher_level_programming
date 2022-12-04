#!/usr/bin/python3
"""100-relationship_states_cities module
contains a script to test the relationship setup between state and cities
"""
from sys import argv

from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_state_with_cities(session):
    """creates a state with cities and adds it to database

    Args:
        session (Session): sqlalchemy session
    """
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
    create_state_with_cities(session)
    session.close()
