#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_6_usa.
It takes 3 arguments: MySQL username, MySQL password, and database name
Results are sorted by states.id in ascending order.
"""
import MySQLdb
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()

if __name__ == "__main__":
    """
    Connects to the MySQL database and retrieves all cities sorted by id.
    Prints each state as a tuple.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    query = "SELECT states.id, states.name FROM states WHERE states.id = 1 ORDER BY states.id ASC"
    cur.execute(query)
    rows = cur.fetchone()
    for row in rows:
        print(row)
    cur.close()
    db.close()
