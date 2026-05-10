# app/api/maintenance.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from app.models.maintenance import MaintenanceHistory
from app.schemas.maintenance import (
    MaintenanceCreate,
    MaintenanceUpdate,
    Maintenance,
)
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Maintenance, status_code=status.HTTP_201_CREATED)
async def create_maintenance(
    maintenance: MaintenanceCreate,
    db: AsyncSession = Depends(get_db),
):
    db_maintenance = MaintenanceHistory(**maintenance.dict())
    db.add(db_maintenance)
    try:
        await db.commit()
        await db.refresh(db_maintenance)
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Maintenance record conflict")
    return db_maintenance

@router.get("/", response_model=list[Maintenance])
async def read_maintenances(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(MaintenanceHistory).offset(skip).limit(limit))
    maintenances = result.scalars().all()
    return maintenances

@router.get("/{maintenance_id}", response_model=Maintenance)
async def read_maintenance(maintenance_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(MaintenanceHistory).where(MaintenanceHistory.id == maintenance_id))
    maintenance = result.scalar_one_or_none()
    if not maintenance:
        raise HTTPException(status_code=404, detail="Maintenance not found")
    return maintenance

@router.put("/{maintenance_id}", response_model=Maintenance)
async def update_maintenance(
    maintenance_id: int,
    maintenance_update: MaintenanceUpdate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(MaintenanceHistory).where(MaintenanceHistory.id == maintenance_id))
    maintenance = result.scalar_one_or_none()
    if not maintenance:
        raise HTTPException(status_code=404, detail="Maintenance not found")
    for key, value in maintenance_update.dict(exclude_unset=True).items():
        setattr(maintenance, key, value)
    await db.commit()
    await db.refresh(maintenance)
    return maintenance

@router.delete("/{maintenance_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_maintenance(maintenance_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(MaintenanceHistory).where(MaintenanceHistory.id == maintenance_id))
    maintenance = result.scalar_one_or_none()
    if not maintenance:
        raise HTTPException(status_code=404, detail="Maintenance not found")
    await db.delete(maintenance)
    await db.commit()
    return None
