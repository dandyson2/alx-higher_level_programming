#!/usr/bin/python3
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""

# Import necessary modules
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Access to the database and get the cities from the database.

    # Define the database URI based on command-line arguments
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Create a database engine
    engine = create_engine(db_uri)

    # Create tables based on the defined models
    Base.metadata.create_all(engine)

    # Create a session for interacting with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object named 'California'
    cal_state = State(name='California')

    # Create a new City object named 'San Francisco' and asso with 'California
    sfr_city = City(name='San Francisco')
    cal_state.cities.append(sfr_city)

    # Add the 'California' State object to the session
    session.add(cal_state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
