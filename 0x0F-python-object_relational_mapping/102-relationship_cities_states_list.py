#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    # Create a database connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and retrieve states with associated cities
    states_with_cities = session.query(State).join(City).order_by(City.id)
    .all()

    # Print the cities and their associated states
    for state in states_with_cities:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))


if __name__ == '__main__':
    main()
