#!/usr/bin/python3
"""9-model_state_filter module
contains a script to filter states
"""
from sys import argv

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def filter_states(session):
    """filters states that contain the letter a

    Args:
        session (Session): sqlalchemey session
    """
    for instance in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        print(instance.id, instance.name, sep=": ")


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    filter_states(session)
