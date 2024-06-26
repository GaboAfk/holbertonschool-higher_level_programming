#!/usr/bin/python3
"""class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
        Create a table "states" with the follow columns:

            - id class attribute that represents a column of an
              auto-generated, unique integer, can't be null and
              is a primary key
            - name class attribute that represents a column of
              a string with maximum 128 characters and can't be
              null
    Args:
        Base (declarative_base): from sqlalchemy.ext.declarative
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(256), nullable=False)
