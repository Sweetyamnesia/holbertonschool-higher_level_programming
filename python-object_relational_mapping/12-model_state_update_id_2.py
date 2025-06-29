#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_6_usa.
It takes 3 arguments: MySQL username, MySQL password and database name
"""

from sqlalchemy import update
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

    stmt = update(State).where(State.id == 2).values(name="New Mexico")
    session.execute(stmt)
    session.commit()

    states = session.query(State).all()
    for state in states:
        print(f"{state.id}: {state.name}")