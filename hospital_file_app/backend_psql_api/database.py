from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_user = "postgres"
db_password = "postgres"
db_server = "localhost:5432"
db_name = "hospital_file_psql_db"

SQLALCHEMY_DATABASE_URL = f'postgresql://{db_user}:{db_password}@{db_server}/{db_name}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()