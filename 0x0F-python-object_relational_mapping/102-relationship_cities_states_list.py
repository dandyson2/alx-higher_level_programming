#!/usr/bin/python3
"""
This script lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # Create a connection to the MySQL database using command-line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to retrieve all State objects and their asso City obj
    states_with_cities = session.query(State).join(City).order_by(City.id)
    .all()

    # Iterate through the results and print City information along with states
    for state in states_with_cities:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
