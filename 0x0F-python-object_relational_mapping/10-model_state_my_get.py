#!/usr/bin/python3
"""
This script prints the State object id
with the name passed as an argument
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Access the database and retrieve a state from it.

    # Construct the database URI using command-line arguments.
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)

    # Create a session to interact with the database.
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for a state with the provided name.
    instance = session.query(State).filter(State.name == argv[4]).first()

    if instance is None:
        print('Not found')
    else:
        print('{0}'.format(instance.id))