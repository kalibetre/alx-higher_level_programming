#!/usr/bin/python3
"""13-model_state_delete_a module
contains a script to delete state from database
"""
from sys import argv

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_matching_states(session, regex):
    """deletes all matching states

    Args:
        session (Session): sqlalchemey session
        regex (str): regex to mach
    """
    session.query(State).filter(
        State.name.like('%{regex}%')).delete(synchronize_session=False)
    session.commit()


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    delete_matching_states(session, regex="Louisiana")
    session.close()
