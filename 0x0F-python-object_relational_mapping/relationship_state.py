#!/usr/bin/python3
"""model_state module
contains the definition for State model
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """States Model

    Args:
        Base (declarative): sqlalchemey declarative base
    """
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="all, delete-orphan")
