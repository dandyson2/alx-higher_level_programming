#!/usr/bin/python3
"""
This script takes an argument and displays all values in the states
where `name` matches the argument from the database `hbtn_0e_0_usa`.
"""

# Import necessary modules
import MySQLdb
from sys import argv


# Check if the script is the main programm
if __name__ == '__main__':
    # Access the database and retrieve states

    # Establish a connection to the database
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        port=3306,
        passwd=argv[2],
        db=argv[3]
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute an SQL query to select states matching the provided name
    cur.execute("SELECT * FROM states WHERE \
            name LIKE BINARY '{}' \
            ORDER BY states.id ASC".format(argv[4]))

    # Fetch all the rows from the query result
    rows = cur.fetchall()

    # Iterate through the rows and print each one
    for row in rows:
        print(row)
