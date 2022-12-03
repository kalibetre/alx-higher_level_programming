#!/usr/bin/python3
"""11-model_state_insert module
contains a script to insert state to database
"""
from sys import argv

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def update_state(session, state_id, state_name):
    """updates a state by name

    Args:
        session (Session): sqlalchemey session
        state_id (int): id of the state
        state_name (str): the updated state name
    """
    existing = session.query(State).filter_by(id=state_id).first()
    if existing is not None:
        existing.name = state_name
        session.commit()


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    update_state(session, state_id=2, state_name="New Mexico")
    session.close()
