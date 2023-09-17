#!/usr/bin/python3
"""
This script deletes all State objects
with a name containing the letter `a`
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Deletes State objects on the database.
    """

    # Construct the database URI
    db_uri = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'

    # Create the database engine
    engine = create_engine(db_uri)

    # Create a session class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Loop through State objects with names containing 'a' and delete them
    for instance in session.query(State).filter(State.name.contains('a')):
        session.delete(instance)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
