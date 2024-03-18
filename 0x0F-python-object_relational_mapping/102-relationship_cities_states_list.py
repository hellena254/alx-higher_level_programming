#!/usr/bin/python3
"""Lists all City objects from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query all City objects and access the linked State object to get the state name
    cities = session.query(City).order_by(City.id).all()

    # Display the results
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session
    session.close()
