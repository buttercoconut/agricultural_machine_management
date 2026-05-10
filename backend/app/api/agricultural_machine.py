from fastapi import APIRouter, HTTPException
from typing import List
from ..models import AgriculturalMachine

router = APIRouter(prefix="/agricultural_machine", tags=["agricultural_machine"])

# In-memory storage for demo purposes
machines: List[AgriculturalMachine] = []

@router.get("/", response_model=List[AgriculturalMachine])
async def read_machines():
    return machines

@router.post("/", response_model=AgriculturalMachine)
async def create_machine(machine: AgriculturalMachine):
    machines.append(machine)
    return machine

@router.get("/{machine_id}", response_model=AgriculturalMachine)
async def read_machine(machine_id: int):
    for m in machines:
        if m.id == machine_id:
            return m
    raise HTTPException(status_code=404, detail="Machine not found")

@router.put("/{machine_id}", response_model=AgriculturalMachine)
async def update_machine(machine_id: int, updated: AgriculturalMachine):
    for idx, m in enumerate(machines):
        if m.id == machine_id:
            machines[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Machine not found")

@router.delete("/{machine_id}")
async def delete_machine(machine_id: int):
    for idx, m in enumerate(machines):
        if m.id == machine_id:
            machines.pop(idx)
            return {"detail": "Deleted"}
    raise HTTPException(status_code=404, detail="Machine not found")
