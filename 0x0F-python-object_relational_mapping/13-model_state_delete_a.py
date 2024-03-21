#!/usr/bin/python3
"""
script deleting States
with names containing 'a'
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')

    Session = sessionmaker(bind=engine)

    session = Session()

    state_letter = 'a'

    state_a = session.query(State).filter(State.name.like(f'%{state_letter}%')).all()
    
    for state in state_a:
        session.delete(state)

    session.commit()
