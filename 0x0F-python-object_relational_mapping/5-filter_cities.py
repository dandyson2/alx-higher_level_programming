#!/usr/bin/python3
"""
This script takes the name of a state as an argument
and lists all cities of that state, using the database `hbtn_0e_4_usa`.
"""

import MySQLdb
from sys import argv


def main():
    # Check if the script is executed as the main program
    if __name__ == '__main__':
        # Access the database and retrieve the cities from it.
        db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                             passwd=argv[2], db=argv[3])

        with db.cursor() as cur:
            # Execute SQL query to get cities of the specified state
            cur.execute("""
                SELECT
                    cities.id, cities.name
                FROM
                    cities
                JOIN
                    states
                ON
                    cities.state_id = states.id
                WHERE
                    states.name LIKE BINARY %(state_name)s
                ORDER BY
                    cities.id ASC
            """, {
                'state_name': argv[4]
            })

            rows = cur.fetchall()

        if rows is not None:
            # Print the list of city names
            print(", ".join([row[1] for row in rows]))


# Call the main function
main()
