from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# SQLAlchemy Database URL
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@host.docker.internal/mekar"
load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a sessionmaker to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our ORM models
Base = declarative_base()

# Model SQLAlchemy untuk data yang akan disimpan di database
class FormDataDB(Base):
    __tablename__ = "form_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    identity_number = Column(Integer, nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    date_of_birth = Column(Date, nullable=False)

# Membuat tabel-tabel di database
Base.metadata.create_all(bind=engine)
