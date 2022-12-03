#!/usr/bin/python3
"""8-model_state_fetch_first module
contains a script to fetch the first states
"""
from sys import argv

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_first_state(session):
    """fetches the first state

    Args:
        session (Session): sqlalchemey session
    """
    instance = session.query(State).first()
    if instance is None:
        print("Nothing")
    else:
        print(instance.id, instance.name, sep=": ")


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    fetch_first_state(session)
