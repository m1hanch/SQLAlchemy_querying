from sqlalchemy.engine import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
username = 'postgres'
password = 'mikel'
host = 'localhost'
port = 5432


engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/school')

if not database_exists(engine.url):
    create_database(engine.url)
Session = sessionmaker(bind=engine)
session = Session()