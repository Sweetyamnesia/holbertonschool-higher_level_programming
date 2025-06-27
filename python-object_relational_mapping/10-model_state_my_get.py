#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_6_usa.
It takes 4 arguments: MySQL username, MySQL password,
database name and state name to search.
Results are sorted by states.id in ascending order.
"""

from sys import argv
from sqlalchemy import create_engine
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = db.create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
    )

    """Bind the engine to a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == argv[4]).first()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")
