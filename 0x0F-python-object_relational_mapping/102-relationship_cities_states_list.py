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
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print City objects
    cities_and_states = session.query(City, State).join(State)
    .order_by(City.id).all()

    for city, state in cities_and_states:
        print("{}: {} -> {}".format(city.id, city.name, state.name))


if __name__ == '__main__':
    main()
