#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # bind the engine to the metadata of the base class so that
    # the declarative can accessed throught the DBsession instance
    Base.metadata.create_all(engine)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # add the state object
    new_state = State(name='Louisiana')
    session.add(new_state)
    new_instance = session.query(State).filter_by(name='Louisiana').first()
    print(new_instance.id)
    session.commit()
