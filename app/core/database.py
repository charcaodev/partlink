import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# -------------------------
# Load environment variables
# -------------------------
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in environment variables")

# -------------------------
# SQLAlchemy setup
# -------------------------
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # avoids stale connections
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# -------------------------
# Dependency for FastAPI
# -------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()