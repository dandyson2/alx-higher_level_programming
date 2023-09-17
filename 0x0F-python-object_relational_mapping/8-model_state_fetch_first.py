#!/usr/bin/python3
"""
This script retrieves and prints the first State object
from the database `hbtn_0e_6_usa`.
"""

# Import necessary modules
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Construct the database URI
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Create the database engine
    engine = create_engine(db_uri)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the first state from the database
    instance = session.query(State).order_by(State.id).first()

    # Check if a state was found and print it
    if instance is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(instance.id, instance.name))
