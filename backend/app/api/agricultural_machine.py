# app/api/agricultural_machine.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from app.models.agricultural_machine import AgriculturalMachine
from app.schemas.agricultural_machine import (
    AgriculturalMachineCreate,
    AgriculturalMachineUpdate,
    AgriculturalMachine,
)
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=AgriculturalMachine, status_code=status.HTTP_201_CREATED)
async def create_machine(
    machine: AgriculturalMachineCreate,
    db: AsyncSession = Depends(get_db),
):
    db_machine = AgriculturalMachine(**machine.dict())
    db.add(db_machine)
    try:
        await db.commit()
        await db.refresh(db_machine)
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Machine already exists")
    return db_machine

@router.get("/", response_model=list[AgriculturalMachine])
async def read_machines(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(AgriculturalMachine).offset(skip).limit(limit))
    machines = result.scalars().all()
    return machines

@router.get("/{machine_id}", response_model=AgriculturalMachine)
async def read_machine(machine_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(AgriculturalMachine).where(AgriculturalMachine.id == machine_id))
    machine = result.scalar_one_or_none()
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    return machine

@router.put("/{machine_id}", response_model=AgriculturalMachine)
async def update_machine(
    machine_id: int,
    machine_update: AgriculturalMachineUpdate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(AgriculturalMachine).where(AgriculturalMachine.id == machine_id))
    machine = result.scalar_one_or_none()
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    for key, value in machine_update.dict(exclude_unset=True).items():
        setattr(machine, key, value)
    await db.commit()
    await db.refresh(machine)
    return machine

@router.delete("/{machine_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_machine(machine_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(AgriculturalMachine).where(AgriculturalMachine.id == machine_id))
    machine = result.scalar_one_or_none()
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    await db.delete(machine)
    await db.commit()
    return None
