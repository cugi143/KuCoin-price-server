from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# Use SQLite in-memory database, echo SQL statements for debugging
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)