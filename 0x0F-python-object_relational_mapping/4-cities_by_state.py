#!/usr/bin/python3
"""
This script lists all cities from the database `hbtn_0e_4_usa`.
"""

import MySQLdb
import sys


def main():
    """
    Access the database and retrieve the cities.
    """

    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> \
                <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", user=username, port=3306,
                             passwd=password, db=database)

        with db.cursor() as cur:
            cur.execute("""
                SELECT
                    cities.id, cities.name, states.name
                FROM
                    cities
                JOIN
                    states
                ON
                    cities.state_id = states.id
                ORDER BY
                    cities.id ASC
            """)

            rows = cur.fetchall()

        if rows:
            for row in rows:
                print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    finally:
        if db:
            db.close()


if __name__ == '__main__':
    main()
