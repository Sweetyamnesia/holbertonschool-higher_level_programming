#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.
It takes 4 arguments: MySQL username, MySQL password,
database name, and state name.
Results are sorted by cities.id in ascending order.
"""

import MySQLdb
import sys

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
    state = sys.argv[4]
    query = "SELECT cities.name"
    "FROM cities"
    "JOIN states ON cities.state_id = states.id"
    "WHERE states.name = %s"
    "ORDER BY cities.id ASC"
    cur.execute(query, (state,))
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    cur.close()
    db.close()
