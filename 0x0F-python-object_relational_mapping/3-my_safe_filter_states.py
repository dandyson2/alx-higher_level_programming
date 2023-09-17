#!/usr/bin/python3
"""
This script takes an argument and displays all values in the states
where `name` matches the argument from the database `hbtn_0e_0_usa`.

This script is designed to prevent SQL injection.
"""

import MySQLdb
import sys


def main():
    """
    Access the database and retrieve states that match the given name.
    """

    if len(sys.argv) != 5:
        print("Usage: {} <DB user> <DB password> \
                <DB name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    user, password, db_name, name_to_match = sys.argv[1:5]

    try:
        db = MySQLdb.connect(host="localhost", user=user, port=3306,
                             passwd=password, db=db_name)
    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        sys.exit(1)

    with db.cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM states
            WHERE name LIKE BINARY %(name)s
            ORDER BY id ASC
        """, {'name': name_to_match})

        rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)

    db.close()


if __name__ == '__main__':
    main()
