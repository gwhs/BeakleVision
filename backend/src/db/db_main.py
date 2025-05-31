import os
from sqlalchemy import create_engine

engine = create_engine(os.environ['DATABASE_URL'])
engine.connect()
