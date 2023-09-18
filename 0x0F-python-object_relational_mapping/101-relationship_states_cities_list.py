#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects contained in the DB
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # Create a MySQL engine with arguments from command line
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create tables based on the models defined in relationship_state
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to retrieve State and City objects
    states_and_cities = session.query(State).outerjoin(City)
    .order_by(State.id, City.id).all()

    # Loop through the results and print them
    for state in states_and_cities:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
