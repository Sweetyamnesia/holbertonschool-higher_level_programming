#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes 4 arguments: mysql username, mysql password,
database name and state name searched.
Results are sorted by states.id in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to the MySQL database and retrieves all states sorted by id.
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
    """
    Use %s to securely pass the variable to the query
    """
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC".format(state)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
