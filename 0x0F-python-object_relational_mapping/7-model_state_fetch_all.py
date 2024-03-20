#!/usr/bin/python3
"""
script that lists all State objects from the database
"""


import sys
from model_state import Base,State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)

    # create a session object
    session = Session()

    # query the database to get all records from the State table
    states = session.query(State).all()

    for state in states:
        print('{}: {}'.format(state.id, state.name))
