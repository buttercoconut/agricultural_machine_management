# models/agricultural_machine.py
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class AgriculturalMachine(Base):
    __tablename__ = "agricultural_machines"

    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String(100), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    purchase_date = Column(Date, nullable=False)
    commissioning_time = Column(Float, nullable=True)  # hours
    # Additional fields can be added as needed

    def __repr__(self):
        return f"<AgriculturalMachine(id={self.id}, model={self.model_name})>"
