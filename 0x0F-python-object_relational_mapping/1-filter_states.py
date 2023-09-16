#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        return

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost", user=username, port=3306,
            passwd=password, db=database
        )

        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE name 'N%' ORDER BY id ASC")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if db:
            db.close()


if __name__ == '__main__':
    main()
