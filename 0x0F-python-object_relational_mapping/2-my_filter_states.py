#!/usr/bin/python3
"""
This script takes an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys


def main(argv):
    if len(argv) != 5:
        print("Usage: {} <username> <password> \
                <database> <state_name>".format(argv[0]))
        sys.exit(1)

    username, password, database, state_name = argv[1], argv[2], argv[3],
    argv[4]

    try:
        db = MySQLdb.connect(host="localhost", user=username, port=3306,
                             passwd=password, db=database)

        cur = db.cursor()
        cur.execute("SELECT * FROM states \
                WHERE name LIKE BINARY %s ORDER BY id ASC", (state_name,))
        rows = cur.fetchall()

        for row in rows:
            print(row)

        db.close()
    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)
