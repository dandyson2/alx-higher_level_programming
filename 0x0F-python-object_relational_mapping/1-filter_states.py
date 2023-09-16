#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv


def list_states_with_N():
    try:
        # Establish a database connection
        db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                             passwd=argv[2], db=argv[3])

        # Create a cursor object
        cur = db.cursor()

        # Execute the SQL query
        cur.execute("SELECT * FROM states WHERE name .. 'N%' ORDER BY id ASC")

        # Fetch all the rows as a list of tuples
        rows = cur.fetchall()

        # Print the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the database connection, whether there's an error or not
        db.close()


if __name__ == '__main__':
    list_states_with_N()
