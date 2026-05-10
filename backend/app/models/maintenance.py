# app/models/maintenance.py
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MaintenanceHistory(Base):
    __tablename__ = "maintenance_history"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer, ForeignKey("agricultural_machines.id"), nullable=False)
    maintenance_date = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    cost = Column(Float, default=0.0)
    parts_replaced = Column(String)  # comma separated part ids or names

    def __repr__(self):
        return f"\u003cMaintenanceHistory id={self.id} machine_id={self.machine_id}\u003e"
