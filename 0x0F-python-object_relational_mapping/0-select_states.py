#!/usr/bin/python3
"""
This script lists all states from the database `hbtn_0e_0_usa`.
"""

import sys
import MySQLdb

def main():
    """
    Access the database and retrieve the states.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", user=username, port=3306,
                             passwd=password, db=database)

        cur = db.cursor()
        cur.execute("SELECT * FROM states")
        rows = cur.fetchall()

        for row in rows:
            print(row)

        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        sys.exit(1)

if __name__ == '__main__':
    main()
