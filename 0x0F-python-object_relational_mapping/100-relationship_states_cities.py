#!/usr/bin/python3
"""
that creates the State “California” with the City “San Francisco”
"""

import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ = "__main__":
    # connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # bind the engine to the metadata of the Base class so that
    # the declaratives can be accessed through a DBsession instance
    Base.metadata.create_all(engine)

    # create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # create the state "California"
    california = State(name="California")

    # Create the City "San Francisco" linked to "California"
    san = City(name="San Francisco")

    # add both objects to the session
    california.cities.append(san)
    session.add(california)

    # commit the chanages
    session.commit()

    # close the session
    session.close()
