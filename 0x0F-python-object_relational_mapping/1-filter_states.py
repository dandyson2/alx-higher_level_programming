#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv


def list_states_with_letter_n(username, password, database_name):
    """
    Access the database and retrieve the states
    with names starting with 'N'.
    """
    try:
        db = MySQLdb.connect(host="localhost", user=username, port=3306,
                             passwd=password, db=database_name)

        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name .. 'N%' ORDER BY id ASC")
        rows = cur.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if db:
            db.close()


if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: ./script.py <username> <password> <database_name>")
    else:
        username, password, database_name = argv[1], argv[2], argv[3]
        list_states_with_letter_n(username, password, database_name)
