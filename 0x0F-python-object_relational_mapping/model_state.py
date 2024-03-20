#!/usr/bin/python3


import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # creates an engine to connect to the database
    engine = create_engine(f'msqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')

    # Create tables in the database
    Base.metadata.create_all(engine)
