from fastapi import APIRouter, HTTPException
from typing import List
from ..models import Maintenance

router = APIRouter(prefix="/maintenance", tags=["maintenance"])

maintenances: List[Maintenance] = []

@router.get("/", response_model=List[Maintenance])
async def read_maintenances():
    return maintenances

@router.post("/", response_model=Maintenance)
async def create_maintenance(m: Maintenance):
    maintenances.append(m)
    return m

@router.get("/{maintenance_id}", response_model=Maintenance)
async def read_maintenance(maintenance_id: int):
    for m in maintenances:
        if m.id == maintenance_id:
            return m
    raise HTTPException(status_code=404, detail="Maintenance not found")

@router.put("/{maintenance_id}", response_model=Maintenance)
async def update_maintenance(maintenance_id: int, updated: Maintenance):
    for idx, m in enumerate(maintenances):
        if m.id == maintenance_id:
            maintenances[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Maintenance not found")

@router.delete("/{maintenance_id}")
async def delete_maintenance(maintenance_id: int):
    for idx, m in enumerate(maintenances):
        if m.id == maintenance_id:
            maintenances.pop(idx)
            return {"detail": "Deleted"}
    raise HTTPException(status_code=404, detail="Maintenance not found")
