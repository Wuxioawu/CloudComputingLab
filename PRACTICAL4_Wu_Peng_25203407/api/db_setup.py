import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
POSTGRES_DB = os.getenv("POSTGRES_DB", "student")
DATABASE_HOST = "database"  
DATABASE_PORT = "5432"

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{POSTGRES_DB}"

print(f"Connecting to database: {SQLALCHEMY_DATABASE_URL}")

# Create the SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()

# Database dependency function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()