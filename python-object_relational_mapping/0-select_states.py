#!/usr/bin/python3
# Import MySQLdb module to connect to a MySQL database
import MySQLdb

# Import sys module to get command-line arguments
import sys

# Execute only if the script is run directly (not imported)
if __name__ == "__main__":
    # Connect to the MySQL database using arguments:
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to execute SQL queries
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
