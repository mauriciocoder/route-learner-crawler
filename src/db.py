from sqlalchemy import create_engine
import os

DATABASE_URI = os.environ['DB_URI']
DB_VERBOSE = os.environ['DB_VERBOSE'] == 'True'
engine = create_engine(DATABASE_URI, echo=DB_VERBOSE)

