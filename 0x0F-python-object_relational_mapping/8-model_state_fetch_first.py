#!/usr/bin/python3
"""
script printing the first object (record) in the states table
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    Session = sessionmaker(bind=engine)

    # create session object
    session = Session()
    
    # query for the first record/object inthe states table
    first_state = session.query(State).first()

    # checking if first_state has a value
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print('Nothing')
