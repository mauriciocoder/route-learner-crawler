# Add the root directory for absolute import
import sys
import os
sys.path.append('../../.')

# print(f"all environment vairables: {os.environ}")

from src.db import engine
from src.models import * # This is to load all the class
from src.models.base import Base

Base.metadata.create_all(engine) # This will create all of the tables from models


