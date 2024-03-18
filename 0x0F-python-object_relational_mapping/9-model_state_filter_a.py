#!/usr/bin/python3
"""
script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # bind the engine to the metadata of the Base class so that
    # the declarative can be accessed through a DBsession
    Base.metadata.create_all(engine)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query the state object that containe the letter a
    for match_a in session.query(State).filter(State.name.like('%a%')):
        print(match_a.id, match_a.name, sep=": ")
