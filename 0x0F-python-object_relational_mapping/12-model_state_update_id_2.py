#!/usr/bin/python3

"""
Changes the name of a State object from the db
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    updState = session.query(State).filter(State.id == 2).first()

    if updState:
        updState.name = 'New Mexico'
        session.commit()
