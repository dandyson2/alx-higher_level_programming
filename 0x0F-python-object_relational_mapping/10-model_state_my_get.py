#!/usr/bin/python3
"""
This script retrieves and prints the ID of a State object
with the name provided as an argument from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    # Check if the correct number of command-line arguments is provided
    if len(argv) != 5:
        print("Usage: {} <username> <password> \
                <database> <state_name>".format(argv[0]))
        return

    # Create a database URI using command-line arguments
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Create a database engine
    engine = create_engine(db_uri)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the State object with the given name
    instance = session.query(State).filter(State.name == argv[4]).first()

    # Check if the state was found or not
    if instance is None:
        print('State not found')
    else:
        # Print the State object's id
        print('State ID: {}'.format(instance.id))


if __name__ == "__main__":
    main()
