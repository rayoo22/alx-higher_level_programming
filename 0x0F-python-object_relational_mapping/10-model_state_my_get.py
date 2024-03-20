#!/usr/bin/python3
"""
prints the State object with the name passed as
an argument
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')

    Session = sessionmaker(bind=engine)

    # create session object to enable querying
    session = Session()

    # query to get the state given as argument
    find_state = session.query(State).filter(State.name == f'{sys.argv[4]}').all()

    if find_state:
        for state in find_state:
            print(state.id)
    else:
        print("Not found")
