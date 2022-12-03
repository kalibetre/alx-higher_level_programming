#!/usr/bin/python3
"""11-model_state_insert module
contains a script to insert state to database
"""
from sys import argv

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def insert_state(session, state_name):
    """inserts a sample state by name

    Args:
        session (Session): sqlalchemey session
    """
    new_state = State(name=state_name)
    session.add(new_state)
    session.commit()
    session.refresh(new_state)
    print(new_state.id)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    insert_state(session, state_name="Louisiana")
    session.close()
