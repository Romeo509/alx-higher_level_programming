#!/usr/bin/python3
"""Script that prints all City objects from the
   database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        cities = (
            session.query(City, State)
            .filter(City.state_id == State.id)
            .order_by(City.id)
            .all()
        )

        for city, state in cities:
            print(f"{state.name}: ({city.id}) {city.name}")
