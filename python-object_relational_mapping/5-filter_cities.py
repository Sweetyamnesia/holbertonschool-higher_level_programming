#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_4_usa.
It takes 4 arguments: mysql username, mysql password
database name and state name.
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
    cur.execute("SELECT cities.name FROM cities WHERE state_id=3 ORDER BY id ASC")
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    cur.close()
    db.close()
