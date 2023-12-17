from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from config import DB_ENGINE, DB_ECHO

# Use SQLite in-memory database, echo SQL statements for debugging
engine = create_engine(DB_ENGINE, echo=DB_ECHO)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)