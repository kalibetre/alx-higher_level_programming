#!/usr/bin/python3
"""10-model_state_my_get module
contains a script to get a state by name
"""
from sys import argv

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_state_by_name(session, state_name):
    """gets a state by name

    Args:
        session (Session): sqlalchemey session
        state_name (str): the name of the state
    """
    instance = session.query(State.id).filter(
        State.name == state_name).first()

    if instance is None:
        print("Not found")
    else:
        print(instance.id)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    get_state_by_name(session, state_name=argv[4])
