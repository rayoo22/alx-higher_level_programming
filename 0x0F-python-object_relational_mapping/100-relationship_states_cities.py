#!/usr/bin/python3
"""
creates the State 'California' with the City San Francisco
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')
    Session = sessionmaker(bind=engine)

    session = Session()

    create_state = 
