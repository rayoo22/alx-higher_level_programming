#!/usr/bin/python3
"""
adds the State object "Louisiana" to the states table
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')
    # creating session class
    Session = sessionmaker(bind=engine)

    #create session object
    session = Session()

    # variable containing name of object to be added
    louis = State(name="Louisiana")

    # adding the variable
    session.add(louis)
    session.commit()

    # to print the newly added object by its id
    print(louis.id)
