#!/usr/bin/python3
"""Adds California and San Francisco to the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
           f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California', cities=[City(name='San Francisco')])
    session.add(new_state)
    session.commit()

    session.close()
