from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

username = 'postgres'
password = 'mikel'
host = 'localhost'
port = 5432
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/school')
Session = sessionmaker(bind=engine)
session = Session()