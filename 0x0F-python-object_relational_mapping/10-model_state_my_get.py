#!/usr/bin/python3
"""
Prints the State object with the name passed
as an argument from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Main script execution block.
    """
    if len(sys.argv) != 5:
        print("""Usage: {} <username> <password>
              <database> <state_name>""".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.id).filter(State.name == state_name).first()
    if result:
        print(result[0])
    else:
        print("Not found")

    session.close()
