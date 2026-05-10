# app/models/rental.py
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer, ForeignKey("agricultural_machines.id"), nullable=False)
    renter_name = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    daily_rate = Column(Float, nullable=False)
    total_cost = Column(Float, nullable=False)

    def __repr__(self):
        return f"\u003cRental id={self.id} machine_id={self.machine_id}\u003e"
