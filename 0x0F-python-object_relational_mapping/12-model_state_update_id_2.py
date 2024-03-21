#!/usr/bin/python3
"""
script updating the name of a State
where its id=2
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')

    Session = sessionmaker(bind=engine)

    session = Session()

    state_id = 2

    state_2 = session.query(State).filter(State.id == state_id).all()
    
    for state in state_2:
        state.name = "New Mexico"

    session.commit()
