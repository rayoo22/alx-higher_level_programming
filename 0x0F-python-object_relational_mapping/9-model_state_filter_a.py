#!/usr/bin/python3
"""
script listing State objects/records conataining the letter 'a'
in their names
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}')
    
    Session = sessionmaker(bind=engine)
    # creating session to enable us query
    session = Session()

    letter = 'a'

    # query to get records of states' names with the letter 'a'
    states_with_a = session.query(State).filter(State.name.like(f'%{letter}%')).all()

    # to print the records, checking whether ther are any
    for state in states_with_a:
        print(f'{state.id}: {state.name}')
