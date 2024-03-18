#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    # bind the engine to the metadata ogf the Base class so that the
    # declaratives can be accessed through a DBSession instance
    Base.metadata.create_all(engine)

    # create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # query all state objects and sort them by id in asc
    # display the result
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
