from fastapi import APIRouter, HTTPException
from typing import List
from ..models import Part

router = APIRouter(prefix="/part", tags=["part"])

parts: List[Part] = []

@router.get("/", response_model=List[Part])
async def read_parts():
    return parts

@router.post("/", response_model=Part)
async def create_part(p: Part):
    parts.append(p)
    return p

@router.get("/{part_id}", response_model=Part)
async def read_part(part_id: int):
    for p in parts:
        if p.id == part_id:
            return p
    raise HTTPException(status_code=404, detail="Part not found")

@router.put("/{part_id}", response_model=Part)
async def update_part(part_id: int, updated: Part):
    for idx, p in enumerate(parts):
        if p.id == part_id:
            parts[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Part not found")

@router.delete("/{part_id}")
async def delete_part(part_id: int):
    for idx, p in enumerate(parts):
        if p.id == part_id:
            parts.pop(idx)
            return {"detail": "Deleted"}
    raise HTTPException(status_code=404, detail="Part not found")
