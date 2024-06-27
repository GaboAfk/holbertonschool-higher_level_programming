#!/usr/bin/python3
""" prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    state = session.query(State)\
        .filter(State.name == state_name).order_by(State.id).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    """#python way
    states = session.query(State).order_by(State.id)
    match = False
    for state in states:
        if state_name == state.name:
            match = True
            print(state.id)
            break
    if not match:
        print("Not found")"""

    session.close()
