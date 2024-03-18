#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # bind the engine to the metadata of the Base class so that the
    # declarative can be accessed through a DBSession instance
    Base.metadata.create_all(engine)

    # create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # query the first state object
    first_state = session.query(State).first()

    # check if the first-state is empty
    if first_state is None:
        print("Nothing")
    else:
        print(first_state.id, first_state.name, sep=": ")
