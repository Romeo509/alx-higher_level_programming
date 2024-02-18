#!/usr/bin/python3
"""
Prints the City objects linked to a State with the
name passed as an argument from the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State, City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = sys.argv[4]
    state = session.query(State).filter_by(name=state_name).first()

    if state:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
    else:
        print("State not found in the database")

    session.close()
