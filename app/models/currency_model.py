from sqlalchemy import Column, Integer, String, Float, DateTime, func
from datetime import datetime
from app.models import Base

class Currency(Base):
    """
    SQLAlchemy model for the currencies table.
    """
    __tablename__ = 'currencies'

    id = Column(Integer, primary_key=True)
    currency = Column(String)
    date_ = Column(DateTime, default=datetime.utcnow().replace(microsecond=0))
    price = Column(Float)
    price = Column(Float)