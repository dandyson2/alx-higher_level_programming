#!/usr/bin/python3
"""
This script retrieves and prints the ID of a State object
with the specified name from the 'hbtn_0e_6_usa' database.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Build the database connection URI using command-line arguments
    db_user, db_password, db_name, state_name = argv[1:5]
    db_uri = f'mysql+mysqldb://{db_user}:{db_password}@localhost:3306 \
    /{db_name}'

    # Create a database engine
    engine = create_engine(db_uri)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the State object with the specified name
    state = session.query(State).filter(State.name == state_name).first()

    if state is None:
        print('State not found')
    else:
        print(f'State ID: {state.id}')
