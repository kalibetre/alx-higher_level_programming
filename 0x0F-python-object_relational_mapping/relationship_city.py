#!/usr/bin/python3
"""model_city module
contains the definition for City model
"""
from relationship_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class City(Base):
    """City Model

    Args:
        Base (declarative): sqlalchemey declarative base
    """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False,)
