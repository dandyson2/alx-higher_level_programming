#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects contained in the DB
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
    engine = create_engine(f'mysql+mysqldb://{username}:{password} \
            @localhost:3306/{database}', pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_and_cities = session.query(State).outerjoin(City)
    .order_by(State.id, City.id).all()

    for state in states_and_cities:
        print_state_and_cities(state)


def print_state_and_cities(state):
    print(f"{state.id}: {state.name}")
    for city in state.cities:
        print(f"    {city.id}: {city.name}")


if __name__ == '__main__':
    main()
