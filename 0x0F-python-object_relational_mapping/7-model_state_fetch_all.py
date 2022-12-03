#!/usr/bin/python3
"""7-model_state_fetch_all module
contains a script to list all states
"""
from sys import argv

from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_all_states(session):
    """lists all states

    Args:
        session (Session): sqlalchemey session
    """
    for instance in session.query(State).all():
        print(instance.id, instance.name, sep=": ")


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    list_all_states(session)
