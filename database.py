# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace 'your_database_url' with the actual database UR
# DB_URL = 'sqlite:///C:\\SQL_Sparky\\to\\sp_bank.db'
DB_URL = 'sqlite:///C:/SQL_Sparky/to/sp_bank.db'

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Create the tables
from models import Base
Base.metadata.create_all(engine)
