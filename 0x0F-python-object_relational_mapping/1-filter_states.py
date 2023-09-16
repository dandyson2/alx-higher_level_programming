#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys


def main(argv):
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        sys.exit(1)

    username, password, database = argv[1], argv[2], argv[3]

    try:
        db = MySQLdb.connect(host="localhost", user=username, port=3306,
                             passwd=password, db=database)

        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE \
                name LIKE BINARY 'N%'\
                ORDER BY id ASC")
        rows = cur.fetchall()

        for row in rows:
            print(row)

        db.close()
    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)
