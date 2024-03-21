#!/usr/bin/python3
"""
prints all City objects from the database in the form of 
state_name: (city_id) name
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')

    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(State, City).join(City, State.id == City.state_id)
    for state, city in results:
        print(f'{state.name}: ({city.id}) {city.name}')
