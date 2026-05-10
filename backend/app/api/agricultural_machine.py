# api/agricultural_machine.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete

from ..models.agricultural_machine import AgriculturalMachine
from ..schemas.agricultural_machine import (
    AgriculturalMachineCreate,
    AgriculturalMachineUpdate,
    AgriculturalMachine,
)
from ..config import settings
from ..database import get_async_session

router = APIRouter(prefix="/machines", tags=["AgriculturalMachine"])

@router.post("/", response_model=AgriculturalMachine, status_code=status.HTTP_201_CREATED)
async def create_machine(
    machine_in: AgriculturalMachineCreate,
    db: AsyncSession = Depends(get_async_session),
):
    machine = AgriculturalMachine(**machine_in.dict())
    db.add(machine)
    await db.commit()
    await db.refresh(machine)
    return machine

@router.get("/", response_model=list[AgriculturalMachine])
async def list_machines(db: AsyncSession = Depends(get_async_session)):
    result = await db.execute(select(AgriculturalMachine))
    machines = result.scalars().all()
    return machines

@router.get("/{machine_id}", response_model=AgriculturalMachine)
async def get_machine(machine_id: int, db: AsyncSession = Depends(get_async_session)):
    machine = await db.get(AgriculturalMachine, machine_id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    return machine

@router.put("/{machine_id}", response_model=AgriculturalMachine)
async def update_machine(
    machine_id: int,
    machine_in: AgriculturalMachineUpdate,
    db: AsyncSession = Depends(get_async_session),
):
    machine = await db.get(AgriculturalMachine, machine_id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    for var, value in machine_in.dict(exclude_unset=True).items():
        setattr(machine, var, value)
    db.add(machine)
    await db.commit()
    await db.refresh(machine)
    return machine

@router.delete("/{machine_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_machine(machine_id: int, db: AsyncSession = Depends(get_async_session)):
    machine = await db.get(AgriculturalMachine, machine_id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    await db.delete(machine)
    await db.commit()
    return None
